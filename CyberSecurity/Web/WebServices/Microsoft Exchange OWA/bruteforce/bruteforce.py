#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
import mmap
import time
import queue
import threading
import argparse
import itertools
import traceback

import validators
import requests
import requests_ntlm

from libs import logger


# Initialize logger
log = logger.Logger()

# Disable InsecureRequestWarning for unverified HTTPS request
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


def parse_args():
	def check_arg_threads(value):
		try:
			value = int(value)
		except:
			raise Exception('Buffer size must be a integer')
		if value < 1 or value > 30:
			raise Exception('Buffer size must be an interger between 1 and 30')
		return value
	 
	def check_arg_file(value):
		value = str(value)
		if not os.path.isfile(value):
			raise Exception('Path \"{}\" is not a file'.format(value))
		return value
		
	def check_arg_target(value):
		value = str(value)
		if validators.url(value):
			return value
		else:
			raise Exception('Target must be a valid URL'.format(value))

	def check_arg_order(value):
		value = str(value)
		if (not value == 'parallel') and (not value == 'serie'):
			raise Exception('Mode must be \"serie\" or \"parallel\"'.format(value))
		return value
		
	parser = argparse.ArgumentParser(description='HTTP Auth Bruteforcer')
	group_target = parser.add_mutually_exclusive_group(required=True)
	group_target.add_argument('-t', '--target', type=check_arg_target, help='URL')
	group_target.add_argument('-T', '--targetfile', type=check_arg_file, help='File of URL')
	group_username = parser.add_mutually_exclusive_group(required=True)
	group_username.add_argument('-u', '--username', type=str, help='Username ("username" or "username:password")')
	group_username.add_argument('-U', '--usernamesfile', type=check_arg_file, help='File of usernames ("username" or "username:password")')
	group_password = parser.add_mutually_exclusive_group()
	group_password.add_argument('-p', '--password', type=str, help='Password')
	group_password.add_argument('-P', '--passwordsfile', type=check_arg_file, help='File of passwords')
	parser.add_argument('-w', '--workers', type=check_arg_threads, default=3, help='Number of threads (interger between 1 and 30)')
	parser.add_argument('-o', '--order', type=check_arg_order, default='serie', help='Targets order ("serie" or "parallel")')
	parser.add_argument('-v', '--verbose', action='store_true', help='Verbose')

	args = parser.parse_args()

	return args


class ThreadsafeIterator:
	def __init__(self, it):
		self.it = it
		self.lock = threading.Lock()

	def __iter__(self):
		return self

	def next(self):
		with self.lock:
			return next(self.it)

	def __next__(self):
		return self.next()


def threadsafe_generator(f):
    def g(*a, **kw):
        return ThreadsafeIterator(f(*a, **kw))
    return g

	
@threadsafe_generator
def generate_userpass(username, usernamesfile, password, passwordsfile):
	
	# Mode bruteforce
	if passwordsfile:
		if username:
			with open(passwordsfile, 'r') as fp:
				for (ur, pr) in itertools.product([username], fp):
					u = ur.strip().split(':')[0]
					p = pr.strip().split(':', 1)[-1]
					
					yield (u, p)
					
		elif usernamesfile:
			with open(usernamesfile, 'r') as fu:
				with open(passwordsfile, 'r') as fp:
					for (ur, pr) in itertools.product(fu, fp):
						u = ur.strip().split(':')[0]
						p = pr.strip().split(':', 1)[-1]
						
						yield (u, p)
	
	# Mode authentication
	else:
		if password:
			if username:
				u = username.strip().split(':')[0]
				p = password.strip().split(':', 1)[-1]
				
				yield (u, p)
				
			elif usernamesfile:
				with open(usernamesfile, 'r') as fu:
					for (ur, pr) in itertools.product(fu, [password]):
						u = ur.strip().split(':')[0]
						p = pr.strip().split(':', 1)[-1]
						
						yield (u, p)
						
		else:
			if username:
					u = username.strip().split(':')[0]
					if ':' in username:							
						p = username.strip().split(':', 1)[-1]
					else:
						p = ''
					yield (u, p)
						
			elif usernamesfile:
				with open(usernamesfile, 'r') as fu:
					for (ur,) in itertools.product(fu):
						u = ur.strip().split(':')[0]
						if ':' in ur:
							p = ur.strip().split(':', 1)[-1]
						else:
							p = ''
							
						yield (u, p)


class HTTP_Auth():
	@staticmethod
	def check(url):
		'''
		target = {
			'url': 'https://some-url.com',
			'status code': 401,
			'server': 'Apache',
			'date': 'Server date',
			'authentication type': 'basic',
			'validated': True,
			'error': Exception,
		}
		'''
		
		# Target definition
		target = {
			'url': url,
			'status code': None,
			'server': None,
			'date': None,
			'authentication type': None,
			'validated': None,
			'error': None,
		}
		
		# Target recon
		try:
			resp = requests.get(target['url'], verify=False, timeout=5)
			
			target['status code'] = resp.status_code
			try:
				target['server'] = resp.headers['Server']
				target['date'] = resp.headers['Date']
			except Exception as e:
				pass
			if 'basic' in resp.headers['WWW-Authenticate'].lower():
				target['authentication type'] = 'basic'
			elif 'digest' in resp.headers['WWW-Authenticate'].lower():
				target['authentication type'] = 'digest'
			elif 'ntlm' in resp.headers['WWW-Authenticate'].lower():
				target['authentication type'] = 'ntlm'
			else:
				target['authentication type'] = 'unknown'
				
		except Exception as e:
			target['error'] = e
		
		# Target validation
		if target['error'] is None and (target['authentication type'] is 'basic' or target['authentication type'] is 'digest' or target['authentication type'] is 'ntlm') and target['status code'] == 401:
			target['validated'] = True
				
		return target
	
	@staticmethod
	def test(test):
		'''
		test = {
			'target': {...},
			'username': 'john',
			'password': 'P@ssw0rd!',
			'success': True,
			'error': Exception,
		}
		'''
		
		# Test definition
		target = test['target']
		
		url = target['url']
		username = test['username']
		password = test['password']

		# Perform test
		timeout = 10

		if target['authentication type'] == 'basic':
			auth = requests.auth.HTTPBasicAuth(username, password)
			resp = requests.get(url=url, auth=auth, verify=False, timeout=timeout)

		elif target['authentication type'] == 'digest':
			auth = requests.auth.HTTPDigestAuth(username, password)
			resp = requests.get(url=url, auth=auth, verify=False, timeout=timeout)
					
		elif target['authentication type'] == 'ntlm':
			auth = requests_ntlm.HttpNtlmAuth(username, password)
			resp = requests.get(url=url, auth=auth, verify=False, timeout=timeout)

		# Success assessment
		if resp.status_code == 200:
			test['success'] = True
		else:
			test['success'] = False

		return test


class WorkerFillTestQueue(threading.Thread):
	def __init__(self, queue_test, targets, generator_userpass, order, workers_number):
		super(WorkerFillTestQueue, self).__init__()
		self.queue_test = queue_test
		self.targets = targets
		self.generator_userpass = generator_userpass
		self.order = order
		self.workers_number = workers_number
		
	def run(self):
		# Fill tests queue targets in serie
		if self.order == 'serie':
			for target in self.targets:
				self.generator_userpass, generator_userpass_copy = itertools.tee(self.generator_userpass)
				
				while True:
					try:
						(username, password) = next(generator_userpass_copy)
						
						test = {
							'target': target,
							'username' : username,
							'password': password,
							'success': None,
							'error': None,
						}
						
						self.queue_test.put(test)
						
					except Exception as e:
						break
				
		# Fill tests queue targets in parallel
		elif self.order == 'parallel':
			while True:
				try:
					(username, password) = next(self.generator_userpass)
										
					for target in self.targets:
						test = {
							'target': target,
							'username' : username,
							'password': password,
							'success': None,
							'error': None,
						}
						
						self.queue_test.put(test)
						
				except Exception as e:
					break
					
		for _ in range(self.workers_number):
			self.queue_test.put(None)
				

class WorkerBruteforce(threading.Thread):
	def __init__(self, queue_test, queue_logging):
		super(WorkerBruteforce, self).__init__()
		self.queue_test = queue_test
		self.queue_logging = queue_logging

	def run(self):
		
		while True:
			try:
				test = self.queue_test.get()

				# No more test to perform
				if test is None:
					self.queue_logging.put(None)
					break
					
				# Perform a test
				else:
					test = HTTP_Auth.test(test)
					self.queue_logging.put(test)

			except Exception as e:
				traceback.print_exc()
				print('WorkerBruteforce => {} : {}'.format(type(e), e))
		

class WorkerLogging(threading.Thread):
	def __init__(self, queue_logging, workers_number, verbose):
		super(WorkerLogging, self).__init__()
		
		self.queue_logging = queue_logging
		self.workers_number = workers_number
		self.verbose = verbose
		
		self.count = 0
		self.progress = 0

	def run(self):

		while True:
			if self.count >= self.workers_number:
				break
			
			try:
				test = self.queue_logging.get()
				
				if test is None:
					self.count += 1
					
				else:
					if test['success']:
						log.success('Authentication successful: Username: \"{}\" Password: \"{}\" URL: {}'.format(test['username'], test['password'], test['target']['url']))

					else:
						if self.verbose:
							log.debug('Authentication failed: Username: \"{}\" Password: \"{}\" URL: {}'.format(test['username'], test['password'], test['target']['url']))
					
					self.progress += 1
					
					if self.progress % 10 == 0:
						if self.verbose:
							log.info('Progress : {}'.format(self.progress))
						else:
							log.info('Progress : {}'.format(self.progress), update=True)
				
			except Exception as e:
				traceback.print_exc()
				log.error('WorkerLogging => {} : {}'.format(type(e), e))
				
		log.info('Progress : {} (end)'.format(self.progress))
			
			
def main():

	log.info('--------------------------')
	log.info('~  Bruteforce HTTP Auth  ~')
	log.info('--------------------------')
	log.info('')

	args = parse_args()

	# Check targets
	targets_included = []
	targets_excluded = []

	if args.target:
		target = HTTP_Auth.check(args.target)
		
		if target['validated']:
			targets_included.append(target)
		else:
			targets_excluded.append(target)

	if args.targetfile:
		with open(args.targetfile) as f:
			for line in f:
				target = HTTP_Auth.check(line.strip())
				
				if target['validated']:
					targets_included.append(target)
				else:
					targets_excluded.append(target)
	'''
	TODO: Change HTTP Auth targets printing to a generic target printing (for instance a table of targets)
	'''
	if len(targets_included) > 0:
		log.info('Included in bruteforce scope:')
		log.info('')
		for target in targets_included:
			log.info('=> URL: {}'.format(target['url']))
			log.info('   Status code: {}'.format(target['status code']))
			log.info('   Server: {}'.format(target['server']))
			log.info('   Date: {}'.format(target['date']))
			log.info('   Authentication type: {}'.format(target['authentication type']))
			log.info('')

	if len(targets_excluded) > 0:
		log.info('Excluded from bruteforce scope:')
		log.info('')
		for target in targets_excluded:
			log.info('=> URL: {}'.format(target['url']))
			log.info('   Status code: {}'.format(target['status code']))
			log.info('   Server: {}'.format(target['server']))
			log.info('   Date: {}'.format(target['date']))
			log.info('   Authentication type: {}'.format(target['authentication type']))
			log.info('')

	if len(targets_included) > 0:
		# Ask for bruteforce validation
		validation = log.input('Launch bruteforce on included targets [y/N] ? ')
		log.info('')

		if not validation.lower() == 'y':
			log.info('Bruteforce not launch')
			exit(0)

		# Bruteforce (multithreaded)
		queue_test = queue.Queue(maxsize=10*args.workers)
		queue_logging = queue.Queue()

		generator = generate_userpass(args.username, args.usernamesfile, args.password, args.passwordsfile)

		wftq = WorkerFillTestQueue(queue_test, targets_included, generator, args.order, args.workers)
		wftq.start()

		wl = WorkerLogging(queue_logging, args.workers, args.verbose)
		wl.start()

		for _ in range(args.workers):
			wb = WorkerBruteforce(queue_test, queue_logging)
			wb.start()

		wl.join()
	
	else:
		# No target to bruteforce
		log.info('No target to bruteforce')
	
	log.info('')
	log.info('Finished')


if __name__ == '__main__':
	main()
