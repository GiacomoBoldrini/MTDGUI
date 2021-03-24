from flask import Flask, send_from_directory
from flask_socketio import SocketIO
import os

#open sockets betweeen client and server, avoid get post but creates a continuous stream of ddata between server and client
socketio = SocketIO(logger=True, engineio_logger=True) 

def createApp():
    
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "FCVG6578BHJNKMLJHGF5678"

    #define blueprints before init app 
    socketio.init_app(app,async_mode='threading')

    @app.route("/")
    def home():
        return {"message": "Hello World!"}, 200

    return app



