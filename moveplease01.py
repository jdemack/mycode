#!/usr/bin/env python3

# import shell utilities and os module
import shutil
import os

## force program to start in home directory
os.chdir('/home/student/mycode/')

## move raynor.obj to /ceph_storage/ folder
#shutil.move('raynor.obj', 'ceph_storage/')

## Ask user to provide new filename for kerrigan.obj
xname = input('What is the new name for kerrigan.obj? ')

## Rename kerrigan.obj to xname value from user input statement
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

