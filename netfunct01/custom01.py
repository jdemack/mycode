#!/usr/bin/env python3

# function to push commands
def commandpush(devicecmd): # devicecmd==list 
    for coffeetime in devicecmd:
        # we'll learn to write code that connects to devices here
        print('\nConnecting to...' + coffeetime)
        print('REBOOTING NOW! --> ')
            # we'll learn to write code that sends cmds to device here

# funtion to iterate through a list of IPs
def devicereboot(iplist):
    for z in iplist:
        print('Connecting to...' + z + '.' + ' REBOOTING NOW!')

### Start our script
work2do = ["10.1.0.1", "10.2.0.1", "10.3.0.1"] # data that replaces data stored in file
ListOfIPs = ["0.0.0.0", "1.1.1.1", "2.2.2.2", "3.3.3.3"]

print("Welcome to the network device command pusher") # welcome message

## get data set
print("\nData set found\n") # replace with function call that reads in data from file

## run 
commandpush(work2do) # call function to push commands to devices
devicereboot(ListOfIPs)