

import pymongo 
import valorDAO
import sessionDAO
import userDAO
import bottle
import cgi
import re
from bson.json_util import dumps

__author__ = "guineitor.traps236@gmail.com"

@bottle.route('/values/<name>/<group_id>')
def get_value_name(name, group_id):
	cookie = bottle.request.get_cookie("session")
	username = sessions.get_username(cookie)  # see if user is logged in
	if username is None:
		return {"logged":"false"}
	else:
		v = values.get_value_by_user(name, group_id)

		bottle.response.content_type = 'application/json'
		return dumps(v)	

@bottle.post('/add_values/')
def add_value_by_name():
	cookie = bottle.request.get_cookie("session")
	username = sessions.get_username(cookie)  # see if user is logged in

	if username is None:
		return {"logged":"false"}
	else:	
		name = username
		value = bottle.request.forms.get("value")
		group_id = bottle.request.forms.get("group_id")

		v = values.insert_values_by_user(username, float(value), group_id)	
		bottle.response.content_type = 'application/json'
		return dumps(v)

@bottle.get('/logout')
def process_logout():
    cookie = bottle.request.get_cookie("session")
    sessions.end_session(cookie)
    bottle.response.set_cookie("session", "")

@bottle.post('/signup')
def process_signup():

    email = bottle.request.forms.get("email")
    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")
    verify = bottle.request.forms.get("verify")

    # set these up in case we have an error case
    errors = {'username': cgi.escape(username), 'email': cgi.escape(email)}
    if validate_signup(username, password, verify, email, errors):

        if not users.add_user(username, password, email):
            # this was a duplicate
            errors['username_error'] = "Username already in use. Please choose another"
            return dumps(errors)

        #session_id = sessions.start_session(username)
        bottle.response.content_type = 'application/json'
        return dumps({'succes':1})
        print session_id
        bottle.response.set_cookie("session", session_id)
        
    else:
        print "user did not validate"
        return dumps(errors)

 #def aux in the user validation       
def validate_signup(username, password, verify, email, errors):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    PASS_RE = re.compile(r"^.{3,20}$")
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

    errors['username_error'] = ""
    errors['password_error'] = ""
    errors['verify_error'] = ""
    errors['email_error'] = ""

    if not USER_RE.match(username):
        errors['username_error'] = "invalid username. try just letters and numbers"
        return False

    if not PASS_RE.match(password):
        errors['password_error'] = "invalid password."
        return False
    if password != verify:
        errors['verify_error'] = "password must match"
        return False
    if email != "":
        if not EMAIL_RE.match(email):
            errors['email_error'] = "invalid email address"
            return False
    return True  

@bottle.post('/login')
def process_login():
    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")

    print "user submitted ", username, "pass ", password

    user_record = users.validate_login(username, password)
    if user_record:
        # username is stored in the user collection in the _id key
        session_id = sessions.start_session(user_record['_id'])
        if session_id is None:
            dumps("/internal_error")

        cookie = session_id
        bottle.response.set_cookie("session", cookie)
        return dumps({'username':user_record['_id']})
    else:
        return dumps("invalid Login")

@bottle.post('/final')
def get_final_result():
    group_id = bottle.request.forms.get("group_id")
    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)  # see if user is logged in
    if username is None:
        return {"logged":"false"}
    else:
        
        sum_by_group = values.get_sum_by_group(group_id)
        list_user_by_group = values.get_count_users_by_group(group_id)
        values.save_final(list_user_by_group, sum_by_group, group_id)
    bottle.response.content_type = 'application/json'
    return dumps(list_user_by_group)

@bottle.get('/final/<group_id>')
def show_final_result(group_id):
    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)  # see if user is logged in
    if username is None:
        return {"logged":"false"}
    else:
        final = values.get_final(group_id)
    bottle.response.content_type = 'application/json'
    return dumps(final)
    return dumps()




connection_string = "mongodb://127.0.0.1"
connection = pymongo.MongoClient(connection_string)
database = connection.test

# valors = valorsDAO.valorsDAO(database)
values = valorDAO.ValorDAO(database)
sessions = sessionDAO.SessionDAO(database)
users = userDAO.UserDAO(database)


bottle.debug(True)
bottle.run(host='0.0.0.0', port=8080) 




