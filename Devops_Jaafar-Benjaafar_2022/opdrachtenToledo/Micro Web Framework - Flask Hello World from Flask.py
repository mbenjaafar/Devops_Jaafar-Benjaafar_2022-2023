#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!pip install flask
#!pip install Faker
# WSGI is a standard described on PEP 3333 and basically, provides a standard interface 
# between web applications written in Python and Webservers. 
# That means, WSGI gives portability to your Python Web Application across many different Web Servers, 
# without any additional configurations on your NGINX, Apache, etc.
##### TO DO: implement this script in Docker
from flask import Flask
#import flask
from datetime import datetime
from faker import Faker
#
app = Flask(__name__)
fake = Faker()
#
#fake.name()
#fake.address()

@app.route('/status/<device_id>')
def dev_status(device_id):
   return { "system": 1, "device": str(device_id) }

@app.route('/time')
def time(): 
   current_time = datetime.now().isoformat(' ')
   return {"system": 1, "datetime": current_time}

@app.route('/<name>')
def hello_name(name):
    return "Hello {}! Do you know {}?".format(name, fake.name())

@app.route('/fake')
def fake_person():
    return "Do you know {}?".format(fake.name())

@app.route('/')
def hello():
    return "Hello World!\n From Flask"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

