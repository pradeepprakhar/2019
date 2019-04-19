#!/usr/bin/python
#import os
import subprocess

f1=open("test.txt","w")
subprocess.call(["ls","-l"],stdout=f1)

