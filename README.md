# Chat-Web-App

## Setup

Ensure you have python 3.6+ installed.

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
cd website
python main.py
```

## Clearing Message History

To clear the message history simply delete the `messages.db` file.

## Old Message Server

Before using socketio for this project I coded out a custom message server that uses standard python sockets. The code for this is located in `old_msg_server/`.

