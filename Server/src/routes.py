from flask import Blueprint, jsonify, current_app
from flask_socketio import emit, join_room, leave_room
from flask import request
from . import socketio
from bs4 import BeautifulSoup as Soup
from .DBManager import DBMan
from src.Controller import GuiController

router = Blueprint("router", __name__)
dbman = DBMan()
run_control = GuiController(socketio)

# Standard socket connection and disconnection of clients
clients = 0
@socketio.on("connect", namespace="/")
def connect():
    global clients
    clients += 1
    print("CLIENTS ", clients)
    socketio.emit('updateSockets', {"clients": clients})

@socketio.on("disconnect", namespace="/")
def disconnect():
    global clients
    clients -= 1
    print("CLIENTS ", clients)
    socketio.emit('updateSockets', {"clients": clients})


# DB Actions Service

@router.route("/getServices", methods=["GET"])
def return_services():
    service_list = dbman.GetAllServices()
    return jsonify({"service_list":service_list, "msg":"service list received from db"})

@router.route("/postService", methods=["POST"])
def post_service():
    body = request.get_json()
    success = dbman.PostService(body)
    if success:
        return jsonify({"msg":"successful insertion of the entry"}), 201
    else:
        return jsonify({"msg":"could not insert entry in db"}), 500

@router.route("/deleteService", methods=["DELETE"])
def delete_service():
    body = request.get_json()
    success = dbman.DeleteService(body['_id'])
    if success:
        return jsonify({"msg":"successful deletion of the entry"}), 200
    else:
        return jsonify({"msg":"could not delete entry in db"}), 500

@router.route("/putService", methods=["PUT"])
def put_service():
    body = request.get_json()['data']
    success = dbman.PutService(body)
    if success:
        return jsonify({"msg":"successful deletion of the entry"}), 200
    else:
        return jsonify({"msg":"could not delete entry in db"}), 500



# DB Actions Runs

@router.route("/getRuns", methods=["GET"])
def return_runs():
    run_list = dbman.GetAllRuns()
    return jsonify({"run_list":run_list, "msg":"run list received from db"})

@router.route("/postRun", methods=["POST"])
def post_run():
    body = request.get_json()
    success = dbman.PostRun(body)
    if success:
        return jsonify({"msg":"successful insertion of the entry"}), 201
    else:
        return jsonify({"msg":"could not insert entry in db"}), 500

@router.route("/deleteRun", methods=["DELETE"])
def delete_run():
    body = request.get_json()
    success = dbman.DeleteRun(body['_id'])
    if success:
        return jsonify({"msg":"successful deletion of the entry"}), 200
    else:
        return jsonify({"msg":"could not delete entry in db"}), 500

@router.route("/putRun", methods=["PUT"])
def put_run():
    body = request.get_json()['data']
    success = dbman.PutRun(body)
    if success:
        return jsonify({"msg":"successful deletion of the entry"}), 200
    else:
        return jsonify({"msg":"could not delete entry in db"}), 500
    
    
    
# Gui controlled actions

@router.route('/actions/initialize',methods=['POST'])
def initialize():
    result, msg = run_control.initialize()
    #socketio.emit('updateAll')
    return jsonify({"newstate":result, "msg":msg})

@router.route('/actions/configure',methods=['POST'])
def configure():
    params = request.get_json(force=True)
    result, msg = run_control.configure(params)
    #socketio.emit('updateAll')
    return jsonify({"newstate":result, "msg":msg})

@router.route('/actions/start',methods=['POST'])
def start():
    result, msg = run_control.start()
    #socketio.emit('updateAll')
    return jsonify({"newstate":result, "msg":msg})

@router.route('/actions/stop',methods=['POST'])
def stop():
    result, msg = run_control.stop()
    #socketio.emit('updateAll')
    return jsonify({"newstate":result, "msg":msg})

@router.route('/actions/pause',methods=['POST'])
def pause():
    result, msg = run_control.pause()
    #socketio.emit('updateAll')
    return jsonify({"newstate":result, "msg":msg})

@router.route('/actions/resume',methods=['POST'])
def resume():
    result, msg = run_control.resume()
    #socketio.emit('updateAll')
    return jsonify({"newstate":result, "msg":msg})

@router.route('/actions/restart',methods=['POST'])
def restart():
    result, msg = run_control.restart()
    #socketio.emit('updateAll')
    return jsonify({"newstate":result, "msg":msg})