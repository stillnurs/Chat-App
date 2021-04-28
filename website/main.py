from flask_socketio import SocketIO
from application import create_app
from application.database import DataBase
import config
import eventlet
eventlet.monkey_patch()


# SETUP
app = create_app()
socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins='*')  # used for user communication


# COMMUNICATION FUNCTIONS

@socketio.on('event', namespace='/')
def handle_my_custom_event(json, methods=None):
    """
    handles saving messages once received from web server
    and sending message to other clients
    :param json: json
    :param methods: ['POST', 'GET']
    :return: None
    """
    if methods is None:
        methods = ['GET', 'POST']
    data = dict(json)
    if "name" in data:
        db = DataBase()
        db.save_message(data["name"], data["message"])

    socketio.emit('message response', json)


# MAINLINE
if __name__ == "__main__":  # start the web server
    socketio.run(app, debug=str(config.Config.DEBUG),
                 host=str(config.Config.SERVER))
