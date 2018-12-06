#!/usr/bin/env python3

# function to push commands
def commandpush(devicecmd): # devicecmd==list 
    for coffeetime in devicecmd:
        # we'll learn to write code that connects to devices here
        print('\nConnecting to...' + coffeetime)
        print('REBOOTING NOW! --> ')
            # we'll learn to write code that sends cmds to device here

### Start our script
work2do = ["10.1.0.1", "10.2.0.1", "10.3.0.1"] # data that replaces data stored in file

print("Welcome to the network device command pusher") # welcome message

## get data set
print("\nData set found\n") # replace with function call that reads in data from file

## run 
commandpush(work2do) # call function to push commands to devices