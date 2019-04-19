#!/usr/bin/python

cpn_file = open('pradeep.txt')
cpn_version = cpn_file.read().split('\n')
count_lines = len(cpn_file.readlines())

print(count_lines)

