

import sys, traceback
from bson.json_util import dumps 
import datetime

class ValorDAO(object):
	"""docstring for ValorDAO"""
	def __init__(self, database):
		self.db = database
		self.values = database.values

	def insert_values_by_user(self, name, value, group_id):
		try:
			value = {'name':name, 'value':value, 'group_id':group_id, 'date':datetime.datetime.utcnow()}
			self.values.insert(value)
		except:
			print traceback.print_exc(file=sys.stdout)
			return 'fail'
		return 'sucess'		
		
	def get_value_by_user(self, name, group_id):
		try:
			query = {'name':name, 'group_id': group_id}
			values = self.values.find(query)
			
		except:
			print 'ferrou'
			return None 	
		return values	