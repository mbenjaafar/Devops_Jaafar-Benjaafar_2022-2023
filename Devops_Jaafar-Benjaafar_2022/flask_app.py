import sqlite3
import hashlib  # secure hashes and message digests
from time import ctime
import json
import requests
import urllib.parse
from flask import Flask, redirect, url_for, session, request, jsonify
from flask_oauthlib.client import OAuth
from flask_ngrok import run_with_ngrok
from flask import request
from flask import render_template
import ntplib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

flaskApp = Flask(__name__)
run_with_ngrok(flaskApp)
database = "database.db"
flaskApp.config['GOOGLE_ID'] = "937632115184-49gtf8rtirdg5000g0eiie325k25mpvg.apps.googleusercontent.com"
flaskApp.config['GOOGLE_SECRET'] = "4f_qgKmV4vTwALuWlaLdV6n5"
flaskApp.debug = True
flaskApp.secret_key = 'development'
oauth = OAuth(flaskApp)

google = oauth.remote_app(
    'google',
    consumer_key=flaskApp.config.get('GOOGLE_ID'),
    consumer_secret=flaskApp.config.get('GOOGLE_SECRET'),
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)


@flaskApp.route('/')
def index():
    if 'google_token' in session:
        # me = google.get('userinfo')
        return redirect(url_for('mypage'))
    return redirect(url_for('login'))


@flaskApp.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))


@flaskApp.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('/login'))


@flaskApp.route('/login/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    # me = google.get('userinfo')
    return redirect(url_for('mypage'))
   # return jsonify({"data": me.data})


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')


@flaskApp.route("/loginSQL")
def main():
    return render_template("login.html")


@flaskApp.route("/index")
def home():
    return render_template("index.html")


@flaskApp.route("/mypage")
def mypage():
    return render_template("mypage.html")


@flaskApp.route("/maps")
def maps():
    return render_template("maps.html")


@flaskApp.route("/googlemapssuccess", methods=["POST", "GET"])
def googlemapssuccess():
    error = None
    if request.method == "POST":
        location = request.form["location"]
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        key = "AIzaSyAJGeIANfCVd8MbXsbXqLKXq1bKqX2QVgA"
        uri = url + "?" + "address" + "=" + location + "&" + "key" + "=" + key
        json_data = requests.get(uri).json()
        return json_data
    else:
        error = 'Invalid Method'
    return error


@flaskApp.route("/mapquestssuccess", methods=["POST", "GET"])
def mapquestssuccess():
    error = None
    if request.method == "POST":
        main_api = "https://www.mapquestapi.com/directions/v2/route?"
        key = "th0o4YURLPy443wAxKekVk1OzaNOkJqm"
        fromlocation = request.form["fromlocation"]
        tolocation = request.form["tolocation"]
        url = main_api + \
            urllib.parse.urlencode(
                {"key": key, "from": fromlocation, "to": tolocation})
        json_data = requests.get(url).json()
        return json_data

    else:
        error = 'Invalid Method'
    return error


@flaskApp.route("/ntpserver")
def ntpserver():
    c = ntplib.NTPClient()
    response = c.request('be.pool.ntp.org', version=3)
    return ctime(response.tx_time)


@flaskApp.route("/signupSuccess", methods=["POST", "GET"])
def signupSuccess():
    conn = sqlite3.connect(database)
    cursur = conn.cursor()
    cursur.execute(
        "CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY NOT NULL, password TEXT NOT NULL);")
    conn.commit()
    try:
        usernameSingup = request.form["usernameSingup"]
        hash_value = hashlib.sha3_256(
            request.form['passwordSignup'].encode()).hexdigest()
        cursur.execute(
            "INSERT INTO users(username, password) VALUES(?, ?)", (usernameSingup, hash_value))
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        return "username has been registered."
    msg = "ok"
    return msg


@flaskApp.route("/loginSuccess", methods=["POST", "GET"])
def loginSuccess():
    error = None
    if request.method == "POST":
        password = request.form["password"]
        username = request.form["username"]
        conn = sqlite3.connect(database)
        cursur2 = conn.cursor()
        cursur2.execute(
            "SELECT password FROM Users WHERE username = ?", (username,))
        records = cursur2.fetchone()
        if not records:
            return "not ok"
        records[0] == hashlib.sha256(password.encode()).hexdigest()
        return redirect(url_for('mypage'))
    else:
        error = 'Invalid Method'
    return error


if __name__ == "__main__":
    flaskApp.run()
