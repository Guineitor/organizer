__author_ = "guineitor.traps236@gmail.com"

import sys
from bson.json_util import dumps

class FormulasDAO(object):
	"""docstring for FormulasDAO"""
	def __init__(self, database):
		
		self.db = database
		self.formulas = database.formula


#get values by name given
	def get_value_by_name(self, name):
		if name == "all":
			query = {}
		else:
			query = {"user": name}

		values = self.formulas.find(query)
			
		return values 	

# add a new value with user
	def set_value_by_user(self, name, value, groupId):
		c = int(count_users_by_group(groupId))
		
		
			set_value_by_user_when_doesnt_exists(_valor, 1, 0, user["name"], _grupoId)

			set_value_by_user(name, value, groupId)

		else:
			formulas.update({"grupoId":_grupoId, "user":_nome}, {'$inc':{'mv':_valor}}, upsert=True, multi=False)
			
			T = float(valorTotal(_grupoId))
			VP = float(getValorPorParticipantes( _grupoId))
			
			
			formulas.update({"grupoId":_grupoId}, {"$set":{"t":T,"vp":VP}}, upsert=True, multi=True)

			userList = users.find()

			for user in userList:
				S = float(valorDiferencaPago(user["name"], _grupoId))
				formulas.update({"grupoId":_grupoId, "user":user["name"]}, {'$set':{'s':S}}, upsert=True, multi=False)

		oid = 0
		return oid

	def set_value_by_user_when_doesnt_exists(_t, _np, _mv, _name, _groupId, _s, _vp):
		try:
			doc = formulas.find_and_modify(query={'groupId':_groupId, 'name':_name},
                                       update={'s':_s, 't':_t, 'np':_np,'mv':_mv, 'vp':_vp, 'name':_name,'groupId':_groupId}, 
                                       upsert=True, new=True)	
		except:
			print "ferrou"
			return None
		
		oid = doc["_id"]
		return oid	

	def count_users_by_group(_groupId):
		c = formulas.find({'groupId':_groupId}).count()
		return c	
		