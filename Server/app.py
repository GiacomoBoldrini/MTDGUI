from src import createApp, socketio
import logging

logger = logging.getLogger('webgui_logger')
logger.setLevel(logging.DEBUG)

app = createApp()

if __name__ == '__main__':
    socketio.run(app, port=5000)
