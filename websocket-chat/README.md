# WebSocket Chat Application

This project is a chat application built using Flask and WebSockets. It allows users to send and receive messages in real time, providing a seamless chat experience.

## Project Structure

```
websocket-chat
├── server
│   ├── app.py               # Entry point of the server application
│   ├── chat.py              # Logic for handling chat messages
│   └── __init__.py          # Initializes the server package
├── static
│   ├── css
│   │   └── style.css        # Styles for the chat application
│   ├── js
│   │   └── main.js          # Client-side JavaScript functionality
│   └── img                  # Directory for images used in the chat
├── templates
│   ├── index.html           # Main HTML file for the chat application
│   └── login.html           # HTML file for the login screen
├── .env                      # Environment variables for the application
├── requirements.txt          # Lists dependencies required for the project
└── README.md                 # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd websocket-chat
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your configuration settings.

5. **Run the application**:
   ```
   python server/app.py
   ```

6. **Access the chat application**:
   Open your web browser and go to `http://localhost:5000`.

## Usage Guidelines

- Users can log in through the login screen and start chatting in real time.
- The chat interface allows users to send and receive messages instantly.
- Optional features include sending images and maintaining session states.

## License

This project is licensed under the MIT License.