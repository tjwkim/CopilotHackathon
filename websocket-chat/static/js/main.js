// filepath: /websocket-chat/websocket-chat/static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    // 현재 페이지 경로를 확인
    const path = window.location.pathname;
    
    // 로그인 페이지의 경우
    if (path === '/login') {
        setupLoginPage();
    } 
    // 채팅 페이지의 경우
    else if (path === '/') {
        setupChatPage();
    }
});

function setupLoginPage() {
    const loginForm = document.getElementById('login-form');
    const errorMessage = document.getElementById('error-message');
    
    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        
        // 간단한 검증
        if (username && password) {
            // 세션 스토리지에 사용자 이름 저장
            sessionStorage.setItem('username', username);
            
            // 채팅 페이지로 리디렉션
            window.location.href = '/';
        } else {
            errorMessage.textContent = 'Please enter both username and password.';
        }
    });
}

function setupChatPage() {
    // 사용자 이름 가져오기
    const username = sessionStorage.getItem('username') || 'Anonymous';
    
    // 소켓 연결
    const socket = io('/chat');
    
    // DOM 요소
    const chatMessages = document.getElementById('chat-messages');
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');
    
    // 연결 이벤트
    socket.on('connect', function() {
        console.log('Connected to server');
        
        // 채팅방 참여
        socket.emit('join', { username: username });
    });
    
    // 메시지 수신 이벤트
    socket.on('message', function(data) {
        addMessage(data.username, data.message, data.username === username);
    });
    
    // 시스템 메시지 수신 이벤트
    socket.on('system_message', function(data) {
        addSystemMessage(data.message);
    });
    
    // 사용자 참여 이벤트
    socket.on('user_joined', function(data) {
        addSystemMessage(`${data.username} joined the chat`);
    });
    
    // 사용자 퇴장 이벤트
    socket.on('user_left', function(data) {
        addSystemMessage(`${data.username} left the chat`);
    });
    
    // 메시지 전송 이벤트
    sendButton.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
    
    function sendMessage() {
        const message = messageInput.value.trim();
        if (message) {
            socket.emit('message', { username: username, message: message });
            messageInput.value = '';
        }
    }
    
    function addMessage(username, message, isCurrentUser) {
        const messageElement = document.createElement('div');
        messageElement.className = `message ${isCurrentUser ? 'user' : 'other'}`;
        messageElement.innerHTML = `<strong>${username}:</strong> ${message}`;
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    function addSystemMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.className = 'message system';
        messageElement.textContent = message;
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
}