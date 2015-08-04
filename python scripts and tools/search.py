#!/usr/bin/python
import sys
import os
import re
import os.path


"""
This is like an OOP version of look_inside.py.
It serves as a tool to find words inside files
of and entire directory and subdirectories inside.
Also prints the line number where it found the
searched word.  Besides this funcionality it also
handles exception in case of the file cannot be opened
and uses regular expressions to parse each file.
"""

DEBUG = True 

class DirName(object):
	def __init__(self, dirname=".", what=""):		
		self.dirname = dirname
		self.what = what
		
	def lookFor(self):
		if(self._check()):
			regex = re.compile(str(sys.argv[2]))
			dirTree = os.walk(self.dirname, True)
			for eachDir in dirTree:
				if DEBUG:
					print "*********INSIDE DIRECTORY ", eachDir[0], "*********"
				for eachDirectory in eachDir[1]:
					if DEBUG:
						print "      *********DIRECTORIES INSIDE ", eachDirectory, "*********"
				for eachFile in eachDir[2]:
					if DEBUG:
						print "               *****FILES INSIDE*****", eachFile
					path_to_file = eachDir[0]+os.sep+eachFile
					try:
						fp = open(path_to_file, "r")
					except IOError, e:
						print "IOError on " + str(e.args[0]) + " - " +  str(e.args[1]) 
						continue
					
					lines = fp.readlines()
					line_counter = 0
					for eachLine in lines:
						look_inside = regex.search(eachLine)
						line_counter += 1
						if(look_inside):
							print "@@@@@FOUND IT!!!.  INSIDE THIS FILE:",path_to_file
							print "     *****LINE ",line_counter,": ", eachLine
					fp.close() 					
		else:
			print "If you don't specify something I can't get nothing for you!"
		
	
	def _check(self):
		if(self.what ==  ""):
			print "Please specify what you're looking for, thanks."
			return False
		else:
			return True
			
	
	
if __name__ == '__main__':	
	cur_path = None
	looking_for = None	
	arg_len = len(sys.argv) - 1
	if(arg_len < 2 or arg_len >= 3):
		print "ERROR: YOU MUST ENTER EXACTLY 2 ARGUMENTS, THE PATH AND WHAT YOU'RE LOOKING FOR!"
	else:
		cur_path = sys.argv[1]
		if sys.argv[1] == ".":
			cur_path = os.environ.get("PWD", None)			
		looking_for = sys.argv[2]		
		searchObj = DirName(cur_path, looking_for)
		searchObj.lookFor()
