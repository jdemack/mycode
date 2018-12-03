#!/usr/bin/env python3

#import modules
import shutil
import os

#start in user's home dir
os.chdir('/home/student/mycode/')

#copy stuff
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
shutil.copytree('5g_research/', '5g_research_backup/')

