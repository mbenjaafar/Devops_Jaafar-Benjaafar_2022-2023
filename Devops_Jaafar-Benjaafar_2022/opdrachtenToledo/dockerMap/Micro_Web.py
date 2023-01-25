from flask import Flask
from flask import request

from datetime import datetime
from faker import Faker

app = Flask(__name__)
fake = Faker()


@app.route("/status/<device_id>")
def dev_status(device_id):
    return {"system": 1, "device": str(device_id)}


@app.route("/time")
def time():
    current_time = datetime.now().isoformat(" ")
    return {"system": 1, "datetime": current_time}


@app.route("/<name>")
def hello_name(name):
    return "Hello {}! Do you know {}?".format(name, fake.name())


@app.route("/fake")
def fake_person():
    return "Do you know {}?".format(fake.name())


@app.route("/")
def main():
    return "Hello World! From Flask"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
