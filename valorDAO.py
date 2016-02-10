__author__ = "guineitor.traps236@gmail.com"

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
			return 0
		return 1		
		
	def get_value_by_user(self, name, group_id):
		try:
			query = {'name':name, 'group_id': group_id}
			values = self.values.find(query)
			
		except:
			print 'ferrou'
			return None 	
		return values

	def get_final(self, group_id):
		#get sum group 
		sum_by_group = 0.00
		try:
			pipeline = [{"$group":{"_id": "$group_id", "sum": {"$sum":"$value"}}},{"$match":{"_id":group_id}}]
			result = self.values.aggregate(pipeline)
			result = result["result"]
			for r in result:
				sum_by_group = r["sum"]
			
		except:
			print traceback.print_exc(file=sys.stdout)
			print "ferrou"	
			return  {"final":"ferrou"}


		count_user_by_group = 0
		try:
			pipeline = [{"$match":{"group_id":group_id}}, {"$group":{"_id":"$name", "count":{"$sum":1}}}]
			result = self.values.aggregate(pipeline)
			result = result["result"]
			for r in result:
				count_user_by_group = r["count"]
				print count_user_by_group
		except:
			print traceback.print_exc(file=sys.stdout)
			print "ferrou"	
			return  {"final":"ferrou"}	

		final = {"result":"sucess"}
		return final

	
	def get_sum_by_group(self, group_id):
		sum_by_group = {}
		try:
			pipeline = [{"$group":{"_id": "$group_id", "sum": {"$sum":"$value"}}},{"$match":{"_id":group_id}}]
			result = self.values.aggregate(pipeline)
			result = result["result"]
			# for r in result:
			# 	sum_by_group = r["sum"]
			
		except:
			print traceback.print_exc(file=sys.stdout)
			print "ferrou"	
			return  {"result":"ferrou"}
		return sum_by_group

	def get_count_users_by_group(self, group_id):
		count_user_by_group = {}
		try:
			pipeline = [{"$match":{"group_id":group_id}}, {"$group":{"_id":"$name", "count":{"$sum":1}, "totalName":{"$sum":"$value"}}}]
			result = self.values.aggregate(pipeline)
			count_user_by_group = result["result"]
			print count_user_by_group
		except:
			print traceback.print_exc(file=sys.stdout)
			print "ferrou"	
			return  {"result":"ferrou"}
		return count_user_by_group