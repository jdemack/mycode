#!/usr/bin/env python3

# import csv library
import csv

# create file object 'f' with read permissions
f = open('csv_users.txt', 'r')

# initialize counter
i = 0

# use csv.reader() function to read each line of the file into list 'row'
for row in csv.reader(f):
    i += 1				# increment counter
    filename = 'admin.rc%d'%(i,)	# set filename to admin.rc%d where %d = i
    rcfile = open(filename, 'w')
    print('export OS_AUTH_URL=' + row[0], file=rcfile)
    print('export OS_IDENTITY_API_VERSION=3', file=rcfile)
    print('export OS_PROJECT_NAME=' + row[1], file=rcfile)
    print('export OS_PROJECT_DOMAIN_NAME=' + row[2], file=rcfile)
    print('export OS_USERNAME=' + row[3], file=rcfile)
    print('export OS_USER_DOMAIN_NAME=' + row[4], file=rcfile)
    print('export OS_PASSWORD=' + row[5], file=rcfile)
    rcfile.close()
