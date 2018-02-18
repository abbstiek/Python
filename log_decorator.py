from __future__ import print_function
import time
import logging
import sys

def log(fileName = None):
	def log_dec(func):
		valid = False
		#result = func.__name__
		if fileName != None:
			if type(fileName) == str:
				try:
					fileObject = open(fileName, "a")
				except (IOError, TypeError):
					valid = False
				else:
					valid = True

		if fileName == None or valid == False:
			def wrap_func(*args):
				print ("\n******************************")
				func_name = func.__name__
				print ("Calling function %s" %func_name)
				if args:
					print ("Arguments: ")
					for arg in args:
						print("- ", end = '')
						print(arg, end = '')
						print(" of type ", end = '' )
						print (type(arg).__name__, end = '')
						print(".")
				else:
					print ("No Arguments.")
				print ("Output:")
				start = time.clock()
				output_fun = func(*args)
				end = time.clock()
				exec_time = end - start
				print ("Execution time: ", end = '')
				print ("%0.5f." % exec_time, "s.")
				if output_fun != None:
					print ("Return value: ", end = '')
					print (output_fun, end = '')
					print (" of type ", end = '')
					print (type(output_fun).__name__)
				else:
					print ("No return value.")
				print ("******************************\n")
			return wrap_func
		else:
			def wrap_func2(*args):
                        	fileObject.write("\n******************************")
				func_name2 = func.__name__
        	                fileObject.write("Calling function %s" %func_name2)
                	        if args:
                                	fileObject.write("Arguments: ")
	                                for arg in args:
						fileObject.write("- ", end = '')
						fileObject.write(arg, end = '')
						fileObject.write(" of type ", end = '')
						fileObject.write(type(arg).__name__, end = '')
						fileObject.write(".")
                	        else:
                        	        fileObject.write("No Arguments.")
	                	fileObject.write ("Output: ")
                		start = time.clock()
                		out = func(*args)
	                	end = time.clock()
        	        	fileObject.write ("Execution time: ", (end-start), "s.")
				if out != None:
					fileObject.write ("Return Value", end = '')
					fileObject.write (out, end = '')
					fileObject.write (" of type ", end = '')
					fileObject.write (type(out).__name__)
				else:
					print("No return value.")
                			fileObject.write("******************************\n")
			return wrap_func2

	return log_dec

@log()
def factorial(*num_list):
	results = []
	for number in num_list:
		res = number
		for i in range(number-1,0,-1):
			res = i*res
		results.append(res)
	return results

@log("logger.txt")
def waste_time(a, b, c):
	print("Wasting time.")
	time.sleep(5)
	return a, b, c

@log("logger.txt")
def gcd(a, b):
	print("The GCD of",a, "and", b, "is ", end="")
	while a!=b: 
		if a > b:
			a -= b
		else:
			b -= a
	print(abs(a))
	return abs(a)

@log()
def print_hello():
	print("Hello!")

@log(10)
def print_goodbye():
	print("Goodbye!")

if __name__ == "__main__":
	factorial(4, 5)
	waste_time("one", 2, "3")
	gcd(15,9)
	print_hello()
	print_goodbye()

