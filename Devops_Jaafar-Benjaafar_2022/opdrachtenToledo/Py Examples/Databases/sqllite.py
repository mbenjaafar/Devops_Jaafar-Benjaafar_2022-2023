import pyotp
import sqlite3
import hashlib
import uuid
db_name = 'test.db'
print(db_name)

############### Plain Text #############

#@app.route('/signup/v1', methods=['POST'])
def signup_v1(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_PLAIN
           (USERNAME  TEXT    PRIMARY KEY NOT NULL,
            PASSWORD  TEXT    NOT NULL);''')
    conn.commit()
    try:
        c.execute("INSERT INTO USER_PLAIN (USERNAME,PASSWORD) " +
                  "VALUES ('{0}', '{1}')".format(username, password))  
        conn.commit()
    except sqlite3.IntegrityError:	
        return "username has been registered."
    print('username: ', username, ' password: ', password)
    return "signup success"
	
################## Password Hashing ###################
#@app.route('/signup/v2', methods=['GET', 'POST'])

def signup_v2(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_HASH
           (USERNAME  TEXT    PRIMARY KEY NOT NULL,  
            HASH      TEXT    NOT NULL);''')
    conn.commit()
    try:
        hash_value = hashlib.sha256(password.encode()).hexdigest()
        c.execute("INSERT INTO USER_HASH (USERNAME, HASH) " +
	                  "VALUES ('{0}', '{1}')".format(username, hash_value))	  
        conn.commit()
    except sqlite3.IntegrityError:
        return "username has been registered."
    print('username: ', username, ' password: ', password, ' hash: ', hash_value)
    return "signup_v2 success"

def verify_plain(username, password):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    query = "SELECT PASSWORD FROM USER_PLAIN WHERE USERNAME = '{0}'".format(username)
    c.execute(query)
    records = c.fetchone()
    conn.close()
    if not records:
        return False
    return records[0] == password
	
def verify_hash(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    query = "SELECT HASH FROM USER_HASH WHERE USERNAME = '{0}'".format(username)
    c.execute(query)
    records = c.fetchone()
    conn.close()
	
    if not records:
        return False
    return records[0] == hashlib.sha256(password.encode()).hexdigest()
	
#@app.route('/login/v1', methods=['GET', 'POST'])
def login_v1()
    error = None
    if request.method == 'POST':
        if verify_plain(request.form['username'], request.form['password']):
            error = 'login success'
        else:
            error = 'Invalid username/password'
    else:
        error = 'Invalid Method'
    return error

result1 = signup_v1('Bob', 'Cisco123')
print (result1)
result2 = signup_v2('Bob', 'Net123')
print (result1h)
result3 = verify_plain('Bob', 'Cisco123')
print (result2)
result4 = verify_hash('Bob', 'Net123')
print (result2h)

