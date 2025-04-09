from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

from .chat import *

def create_app():
    return app

if __name__ == "__main__":
    socketio.run(app)