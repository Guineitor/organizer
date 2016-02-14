__author__ = "guineitor.traps236@gmail.com"

import sys, traceback
from bson.json_util import dumps 
import datetime

class ValorDAO(object):
	"""docstring for ValorDAO"""
	def __init__(self, database):
		self.db = database
		self.values = database.values
		self.compiled_values = database.compiled_values

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

	
	def get_sum_by_group(self, group_id):
		sum_by_group = 0.00
		try:
			pipeline = [{"$group":{"_id": "$group_id", "sum": {"$sum":"$value"}}},{"$match":{"_id":group_id}}]
			result = self.values.aggregate(pipeline)
			result = result["result"]
			for r in result:
				sum_by_group = r["sum"]
				

		except:
			print traceback.print_exc(file=sys.stdout)	
			return  None
		return float(sum_by_group)

	def get_count_users_by_group(self, group_id):
		
		list_user_by_group = {}
		try:
			pipeline = [{"$match":{"group_id":group_id}}, {"$group":{"_id":"$name", "totalName":{"$sum":"$value"}}}]
			result = self.values.aggregate(pipeline)
			list_user_by_group = result["result"]
		except:
			print traceback.print_exc(file=sys.stdout)
			return  {"result":"ferrou"}
		return list_user_by_group


	def save_final(self, list_users, sum_by_group, group_id):
		try:
			cnt = 0
			final = []
			final_parse = {}
			count = len(list_users)	
			value_each_person = sum_by_group/count
			print list_users
			for doc in list_users:
				# final_parse["sum"] = sum_by_group
				for key in doc:
					final_parse[key] = doc[key]
					if key == "totalName":
						final_parse["personal_value"] = final_parse["totalName"]- value_each_person
					print str(key)+":"+str(doc[key])
				final_parse["group_id"] = group_id
				final.append(final_parse)	
				final_parse = {}
			self.compiled_values.insert(final)	
		except:
			print traceback.print_exc(file=sys.stdout)	
			return False
		
		print final	
		return True	

	

	def get_final(self, group_id):
		final  = {}
		query = {"group_id":group_id}
		try:
			final = self.compiled_values.find(query)
		except:
			print traceback.print_exc(file=sys.stdout)	
			return False

		return final	
	