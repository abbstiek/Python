"""Abygail Stiekman
	aes15d
	July 21, 2017"""

from __future__ import print_function
from socket import *
import json

class HTTPConnection(object):
	"""This class represents a a connection with an HTTP server"""

	def __init__(self,host,port=80):
		#initializes constructors
		self.host = host
		self.port = port

		self.comp = None
		#the HTTP version used for all requests
		self.version = "HTTP/1.0\r\n"
		#socket to connect
		self.s = socket()
		self.connect()

	def connect(self):
		#connects to the server when the object is created
		self.s.connect((self.host,self.port))

	def request(self,method,url,headers=None):
		#sends a request to the server using the HTTP request method
		print(url)
		request = method + " " + url + " " + self.version + "Host: " + self.host + "\r\n\r\n"

		self.s.send(request)

		self.comp = self.host + url

	def getresponse(self):
		#gets the response from the server. returns
		#an HTTPResponse instance
		return HTTPResponse(self.s)

	def close(self):
		#closes the connection to the server
		self.s.close()

class HTTPResponse(object):
	"""This class holds instances that represent a response returned
	from an HTTP server"""

	def __init__(self,sock):

		#initializer, declares the constructors
		self.s = sock

		#HTTP protocol version used by server.
		self.version = None

		#status code returned by the server
		self.status = None

		#reason phrase returned by the server
		self.reason = None
		self.name = None
		self.data = None
		self.text = None
		
		#true if passes the check
		self.check = False
		self.start = 0
		self.end = 0
		self.dict = {}

		#list that holds headers
		self.headers = []
		self.body = []

		#makefile to communicate with the server
		#reads the response
		self.m = self.s.makefile()
		self.lines = self.m.readline().split()

		#if the version is set to the default, then returns that
		#value, if not sets the version to 1.0
		if "1.1" in self.lines[0]:
			self.version = 1.1
		else:
			self.version = 1.0

		self.status = self.lines[1]
		#if number of lines is greater than 3, pops them
		#separated by spaces
		if len(self.lines) > 3:
			self.lines.pop(0)
			self.lines.pop(0)
			self.reason = ' '.join(self.lines)
		else:
			self.reason = self.lines[2]


		for line in self.m.readlines():
			#pulls from the server
			if "<html>" in line:
				self.check = True
			#pulls from the server
			if "<!doctype html" in line.lower():
				self.check = True
			#if <html> or <!doctype html, add it to the file
			if self.check:
				self.body.append(line)
			#if it cannot be found in self.body then it returns
			#a copy of the string with leading and trailing
			#characters removed
			if not self.body:
				line = line.strip()
			#if the line does not end, adds to the lsit of headers
				if line != '':
					my_list = tuple(line.split(':',1))
					self.headers.append(my_list)

		self.headers = dict(self.headers)

		self.text = ' '.join(self.body)

	def read(self,amt = 0):

		#reads and returns the response body, or up to the next amt
		#of bytes.
		#once the response body has been read, any more calls to read()
		#will return an empty string

		#amt holds the # of bytes to be returned to the response body
		if amt == 0:
			ret = self.text
			self.text = ''
			return ret
		#if the lines to read do not end, continue adding it
		if self.text != '':
			temp = self.text[:amt]
			self.text = self.text[amt:]
			return temp
		#returns info to be read by server
		return self.text

	def getheader(self,name = None):
	#gets the contents of the header name or returns
	#None if the header name is not in the header list of the response

		if name != None:
			return self.headers[name]
		return None

	def getheaders(self):
	#returns a list of (header, value) tuples
	#returns an empty list if no headers are included

		return self.headers
