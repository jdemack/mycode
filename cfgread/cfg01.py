#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
#configfile = open('vlanconfig.cfg', 'r')

## display file to the screen - .read()
#print(configfile.read())

## close file
#configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
#configfile = open('vlanconfig.cfg', 'r')
print('Please enter the filename: ')
configfile = open(input(), 'r')

## make a list of file lines - .readlines()
configlist = configfile.readlines()
#print(configlist)

# initialize counter
counter = 0

## Iterate thrhough configlist
for x in configlist:
    print(x.strip(), end=" ")
    counter += 1

print(counter)

## Always close your file
configfile.close()