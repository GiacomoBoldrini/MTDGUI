from flask import Flask, send_from_directory
from flask_socketio import SocketIO
import os

#open sockets betweeen client and server, avoid get post but creates a continuous stream of ddata between server and client
socketio = SocketIO(logger=True, engineio_logger=True, cors_allowed_origins='http://localhost:8080') 

def createApp():
    
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "FCVG6578BHJNKMLJHGF5678"

    #define blueprints before init app 
    socketio.init_app(app)

    @app.route("/")
    def home():
        return {"message": "Hello World!"}, 200

    @socketio.on('testing')
    def test(data, methods=['GET', 'POST']):
        print(data['message'])

    @socketio.on('connect')
    def hello():
        print("A client connected!")

    @socketio.on('receive')
    def sendmessage():
        socketio.emit('receive', {'message': 'Eureka!'})

    @socketio.on('disconnect')
    def hello():
        print("A client disconnected!")

    return app



