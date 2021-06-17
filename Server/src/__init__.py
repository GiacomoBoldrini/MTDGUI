from flask import Flask, send_from_directory, send_from_directory
from flask_socketio import SocketIO
import os

#open sockets betweeen client and server, avoid get post but creates a continuous stream of ddata between server and client
#socketio = SocketIO(logger=True, engineio_logger=True, cors_allowed_origins='http://localhost:8080', async_mode='threading') 
socketio = SocketIO(logger=True, engineio_logger=True, cors_allowed_origins='http://localhost:8080', async_mode="threading") 

def createApp():
    
    app = Flask(__name__, static_url_path='')
    app.config["SECRET_KEY"] = "FCVG6578BHJNKMLJHGF5678"

    from .routes import router
    app.register_blueprint(router,url_prefix="/api")


    #define blueprints before init app 
    socketio.init_app(app)
    #, async_mode='threading'

    @app.route("/")
    def home():
        return {'msg': 'ciao'}

    return app



