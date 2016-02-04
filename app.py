

import pymongo 
import valorDAO
import sessionDAO
import userDAO
import bottle
from bson.json_util import dumps

__author__ = "guineitor.traps236@gmail.com"

@bottle.route('/values/<name>/<group_id>')
def get_value_name(name, group_id):
	v = values.get_value_by_user(name, group_id)

	bottle.response.content_type = 'application/json'
	return dumps(v)	

@bottle.post('/add_values/')
def add_value_by_name():
	name = bottle.request.forms.get("name")
	value = bottle.request.forms.get("value")
	group_id = bottle.request.forms.get("group_id")


	v = values.insert_values_by_user(name, value, group_id)	
	bottle.response.content_type = 'application/json'
	return dumps(v)

@bottle.get('/signed')
def get_sesison():

	cookie = bottle.request.get_cookie("session")
	session_id = sessions.get_session(cookie)
	return session_id	

connection_string = "mongodb://127.0.0.1"
connection = pymongo.MongoClient(connection_string)
database = connection.test

# valors = valorsDAO.valorsDAO(database)
values = valorDAO.ValorDAO(database)
sessions = sessionDAO.SessionDAO(database)
users = userDAO.UserDAO(database)


bottle.debug(True)
bottle.run(host='0.0.0.0', port=8080) 




