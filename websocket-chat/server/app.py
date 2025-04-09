import os
from flask import Flask, render_template
from flask_socketio import SocketIO
from .chat import ChatNamespace

# 절대 경로를 사용하여 템플릿 및 정적 파일 디렉토리 설정
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

# 소켓 네임스페이스 등록
socketio.on_namespace(ChatNamespace('/chat'))

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')