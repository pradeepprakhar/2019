#!/user/bin/python

def deco(func):
	def new_func(*args, **kwargs):
		print 'in mydeco'
		result=func(*args, **kwargs)
		return result
	return fun_func

deco(addthem(3,4))

