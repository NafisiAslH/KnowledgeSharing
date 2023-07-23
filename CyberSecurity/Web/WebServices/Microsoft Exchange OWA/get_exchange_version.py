import requests
import sys
import warnings
warnings.filterwarnings("ignore")

def buildnumber_to_version(BuildNumber):
#Reference:https://docs.microsoft.com/en-us/Exchange/new-features/build-numbers-and-release-dates?redirectedfrom=MSDN&view=exchserver-2019
	
    strlist = BuildNumber.split('.')

    if int(strlist[0]) == 4:
        return 'Exchange Server 4.0'

    elif int(strlist[0]) == 5:
        if int(strlist[1]) == 0:
            return 'Exchange Server 5.0'
        elif int(strlist[1]) == 5:
            return 'Exchange Server 5.5'

    elif int(strlist[0]) == 6:
        if int(strlist[1]) == 5:
            if int(strlist[2]) == 6944:
                return 'Exchange Server 2003'
            elif int(strlist[2]) == 7226:
                return 'Exchange Server 2003 SP1'
            elif int(strlist[2]) == 7683:
                return 'Exchange Server 2003 SP2'
            elif int(strlist[2]) == 7653:
                return 'Exchange Server 2003 post-SP2'
            elif int(strlist[2]) == 7654:
                return 'Exchange Server 2003 post-SP2'
        elif int(strlist[1]) == 0:
            return 'Exchange 2000 Server'

    elif int(strlist[0]) == 8:
        if int(strlist[1]) == 0:
            return 'Exchange Server 2007'
        elif int(strlist[1]) == 1:
            return 'Exchange Server 2007 SP1'
        elif int(strlist[1]) == 2:
            return 'Exchange Server 2007 SP2'
        elif int(strlist[1]) == 3:
            return 'Exchange Server 2007 SP3'

    elif int(strlist[0]) == 14:
        if int(strlist[1]) == 0:
            return 'Exchange Server 2010'
        elif int(strlist[1]) == 1:
            return 'Exchange Server 2010 SP1'
        elif int(strlist[1]) == 2:
            return 'Exchange Server 2010 SP2'
        elif int(strlist[1]) == 3:
            return 'Exchange Server 2010 SP3'

    elif int(strlist[0]) == 15:        
        if int(strlist[1]) == 0:
            return 'Exchange Server 2013'
        elif int(strlist[1]) == 1:
            return 'Exchange Server 2016'
        elif int(strlist[1]) == 2:
            return 'Exchange Server 2019'

def get_exchange_buildnumber(url):
    try:
        
        r = requests.get(url, verify = False)
        nPos1 = r.text.index('href="')       
        str1 = r.text[nPos1+9:nPos1+40]
        nPos2 = str1.index('/')
        nPos3 = str1.index('/themes/')
        str2 = str1[nPos2:nPos3]
        nPos4 = str2.rindex('/')
        BuildNumber = str2[nPos4+1:]
        print('Build number:%s'%(BuildNumber))
        result = buildnumber_to_version(BuildNumber)
        print(result)
        
    except Exception as e:
         print('[!]Error:%s'%e)

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print('[!]Wrong parameter')
        print('Usage:')
        print('%s <url>'%(sys.argv[0]))
        print('Eg.')
        print('%s https://mail.test.com/owa'%(sys.argv[0]))
        sys.exit(0)
    else:
        get_exchange_buildnumber(sys.argv[1])
    
