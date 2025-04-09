from flask import Blueprint, request
from flask_socketio import SocketIO, Namespace, emit

chat_bp = Blueprint('chat', __name__)
socketio = SocketIO()

class ChatNamespace(Namespace):
    def on_connect(self):
        print('Client connected')
        emit('system_message', {'message': 'Welcome to the chat!'})

    def on_disconnect(self):
        print('Client disconnected')

    def on_message(self, data):
        print('Message received:', data)
        emit('message', data, broadcast=True)

    def on_join(self, data):
        username = data.get('username')
        print(f'{username} joined the chat')
        emit('user_joined', {'username': username}, broadcast=True)

    def on_leave(self, data):
        username = data.get('username')
        print(f'{username} left the chat')
        emit('user_left', {'username': username}, broadcast=True)