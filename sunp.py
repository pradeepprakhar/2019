#/usr/bin/python

import subprocess
subprocess.call("ls")
subprocess.call(["ls","-l"])
subprocess.call(["cat","test.txt"])

