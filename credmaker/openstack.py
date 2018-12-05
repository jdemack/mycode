#!/usr/bin/env python3

# open file admin.rc for writing
outFile = open('admin.rc', 'a')

# prompt user for OS_AUTH_URL
print('What is the OS_AUTH_URL?')
osAuth = input()
print('export OS_AUTH_URL=' + osAuth, file=outFile)
print('export OS_IDENTITY_API_VERSION=3', file=outFile)

# prompt user for OS_PROJECT_NAME
print('What is the OS_PROJECT_NAME?')
osProj = input()
print('export OS_PROJECT_NAME=' + osProj, file=outFile)

# prompt user for OS_PROJECT_DOMAIN_NAME
print('What is the OS_PROJECT_DOMAIN_NAME?')
osProjDom = input()
print('export OS_PROJECT_DOMAIN_NAME=' + osProjDom, file=outFile)

# prompt user for OS_USERNAME
print('What is the OS_USERNAME?')
osUser = input()
print('export OS_USERNAME=' + osUser, file=outFile)

# prompt user for OS_USER_DOMAIN_NAME
print('What is the OS_USER_DOMAIN_NAME?')
osUserDom = input()
print('export OS_USER_DOMAIN_NAME=' + osUserDom, file=outFile)

# prompt user for OS_PASSWORD
print('What is the OS_PASSWORD?')
osPass = input()
print('export OS_PASSWORD=' + osPass, file=outFile)

# close file admin.rc
outFile.close()