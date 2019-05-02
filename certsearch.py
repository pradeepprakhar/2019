#!/usr/bin/python3
import re

START_PATTERN = '-----BEGIN RSA PRIVATE KEY-----'
END_PATTERN = '-----END RSA PRIVATE KEY-----'

with open('file1.txt') as file:
    match = False
    newfile = open('my_new_file.txt', 'w')
    newfile.close()

    for line in file:
        if re.match(START_PATTERN, line):
            match = True
            newfile = open('my_new_file.txt', 'a')
            newfile.write(START_PATTERN)
            newfile.write('\n')
            continue
        elif re.match(END_PATTERN, line):
            match = False
            newfile.write(END_PATTERN)
            newfile.write('\n')
            newfile.close()
            continue
        elif match:
            newfile.write(line)
file.close()
