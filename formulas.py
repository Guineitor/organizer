#
# Copyright (c) 2008 - 2013 10gen, Inc. <http://10gen.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#

import pymongo 
import formulasDAO
import sessionDAO
import userDAO
import bottle
from bson.json_util import dumps

__author__ = "guineitor.traps236@gmail.com"

@bottle.route('/')
def index_app():
	bottle.response.content_type = 'application/json'
	return dumps("{}")

@bottle.route('/values/<name>')
def get_value_name(name = "all"):
	values = formulas.get_value_by_name(name)

	bottle.response.content_type = 'application/json'
	return dumps(values)	
@bottle.post('/add_values/<name>')
def add_value_by_name(name,value,groupId):

	oid = 0
	return dumps(oid)


connection_string = "mongodb://127.0.0.1"
connection = pymongo.MongoClient(connection_string)
database = connection.test

formulas = formulasDAO.FormulasDAO(database)
sessions = sessionDAO.SessionDAO(database)
users = userDAO.UserDAO(database)


bottle.debug(True)
bottle.run(host='0.0.0.0', port=8080) 




