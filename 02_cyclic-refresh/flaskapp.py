import datetime

import gevent
from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("request_time")
def on_request():
    socketio.emit("return_time", {"time": datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")})


socketio.run(app, port=5001)
