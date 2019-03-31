#!/usr/bin/env python

import sys
from tinydb import TinyDB, Query

class Journal_Entry():
	def __init__(self, dr_acct, cr_acct, memo, amount):
#		journal.__init__([])
		self.debit = dr_acct
		self.credit = cr_acct
		self.memo = memo
		self.amount = amount

if "-h" in sys.argv or "--help" in sys.argv:
	print ("This is help text")
else:
	print ("Type -h or --help for help text")

db = TinyDB('db.json')
db.insert({'int':1, 'char': 'a'})
db.insert({'int':2, 'char': 'b'})