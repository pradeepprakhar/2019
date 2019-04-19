#!/usr/bin/python

total = 0;
def sum(arg1,arg2):
	total= arg1 + arg2;
	print "inside the function local total:", total
	return total;
	
sum(10,20);
print"outside the function global total", total

var1 = 'hello world'
var2 = "python programming"

print var1[0]
print var2[1:5]


var3 = 'Hello my World! \a'
print "updated striing := ", var3[:6] + 'Python\a'


list1 = ['physics', 'chemistry', 1997, 2000 ];

list2 = [1,2,3,4,5,6,7];

print "list1[0]: ", list1[3]
print "list2[1:5]: ", list2[1:5]

