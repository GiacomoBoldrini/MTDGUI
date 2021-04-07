from flask import Blueprint, jsonify, current_app
from flask_socketio import emit, join_room, leave_room
from flask import request
from . import socketio
from bs4 import BeautifulSoup as Soup

class dqmEmitter: 

    def __init__: