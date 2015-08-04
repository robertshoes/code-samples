import sys
import os

"""
This an OOP version of look_inside.py
and also receives parameter from the prompt:
a specific directory and the word that you're
looking for.
"""

class DirName(object):
	def __init__(self, dirname=".", what=""):		
		self.dirname = dirname
		self.what = what
		
	def lookFor(self):
		if(self._check()):
			dirTree = os.walk(self.dirname, True)
			for eachDir in dirTree:
				print "*********INSIDE DIRECTORY ", eachDir[0], "*********"
				for eachDirectory in eachDir[1]:
					print "----->*********DIRECTORIES INSIDE ", eachDirectory, "*********"
					
		else:
			print "If you don't specify something I can't get nothing for you!"
		
	
	def _check(self):
		if(self.what == ""):
			print "Please specify what you're looking for, thanks"
			return False
		else:
			return True
			
	
	
if __name__ == '__main__':
	searchObj = DirName(sys.argv[1], sys.argv[2])
	searchObj.lookFor()
	
