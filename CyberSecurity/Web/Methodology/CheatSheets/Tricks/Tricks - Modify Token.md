# Trick - Modify Token

### Description
details
</br>&nbsp;

## Sub Techniques
### 1. Use another user's Token
```
cookie: session=SESSION_A;
token = TOKEN_B
```
### 2. Reuse Token (Check token expiration)
```
First request:
token = TOKEN

Second request:
token = TOKEN
```
### 3. Remove parameter (name and value)
```
remove name and value
```
### 4. Send empty value
```
token = (empty)
```
### 7. Modify a few bits
```
origianl token: TOKEN_123456
forged token: TOKEN_123478
```
### 6. Send null/None value
```
token = None
token = null
```


## References:
[Reference](link)</br>
