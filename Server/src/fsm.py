# AT THE MOMENT THIS IS A COPY OF the templateApp.py from ECAL DAQ
# Cucciati et. al.
# https://gitlab.cern.ch/ecal-daq-upgrade/H4WEBGUI/-/blob/master/Server/src/templateApp.py
from zmq import *
import socket

class FSM:
    """
        A FSM connecting to sockets and controlled by the gui
    """
    def __init__(self):

        self.socket_cycle_running = False
        
        self.states = {
            "Initialize": 1 ,
            "Configure": 2 ,
            "Run": 3 ,
            "Pause": 4 ,
            "Stop": 5,
            "Error": 6,
        }
        
        self.routes = {
            "Initialize": ["Configured", "Error"],
            "Configure": ["Run", "Error"],
            "Run": ["Pause", "Stop", "Error"],
            "Pause": ["Run", "Stop", "Error"],
            "Stop": ["Error"],
            "Error": []
        }
        
        self.currentState = "Initialize"
        self.configuration = {}
        
        self.data_port = 0
        self.status_port = "localhost:8080" #hardcoded
        self.cmd_port = 0

        # https://zeromq.org/socket-api/#publish-subscribe-pattern
        # ZQM subscriber to receive commands from client through sockets
        self.sub = None # Receives commands
        # ZQM publisher to send commands from server to client through sockets
        self.pub = None # Send status 
        self.context = None
        # Poller: https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/multisocket/zmqpoller.html
        # We setup zmq poller to poll for messages on the socket connection to both command server and publisher.
        self.poller = None
        self.sub_urls = []
        
        self.runningFlag = False
        
        # serving messages in a class attribute,easier inheritance
        self.rec_msg = ""
        
    def initialize_zmq_channels(self):
        self.context = Context()
        self.poller = Poller()
        # SUB here is a specific ZQM string, instantiates a SUBscriber instance inside the FSM
        self.sub = self.context.socket(SUB)
        # If the application run in local... do we need to rename the url
        # with localhost instead of machine name? Let's do it...

        # First: subscription to the sockets where the application receives commands
        gui_hostname = socket.gethostname()
        for url in self.sub_urls:
            new_url = "tcp://"
            if gui_hostname in url:
                url = url.replace(gui_hostname,"localhost")
            new_url += url
            self.sub.connect("tcp://"+url)
        # Here we subscribe to an empty topic
        # A subscriber socket can have multiple subscription filters.
        self.sub.setsockopt(SUBSCRIBE,b'')
        self.poller.register(self.sub,POLLIN)

        # Second: generate socket to send status
        self.pub = self.context.socket(PUB)
        new_url = "tcp://*:"
        port_index = self.status_port.find(":")
        new_url = new_url + self.status_port[port_index+1:]
        print("Url to publish app status: ", new_url)
        self.pub.bind(new_url)
        self.poller.register(self.pub,POLLIN)

    def listen_socket(self):
        print("Entering in socket cycle")
        while self.socket_cycle_running:
            try:
                # Limiting the loop rate with 1 sec sleep
                time.sleep(1)
                # Sending state
                status_msg = "STATUS statuscode="+str(self.states[self.currentState])
                print("Sending status msg: ",status_msg)
                self.pub.send_string(status_msg)

                # Polling for messages
                socks = dict(self.poller.poll(1))
                if socks.get(self.sub):
                    self.rec_msg = (self.sub.recv()).decode("utf-8")
                    self.proc_message(self.rec_msg)

                # It seems that python is not flushing "print" each time it is called.
                # Forcing to do it once per cycle.

                sys.stdout.flush()
            except:
                print("Error in the loop. Breaking...")
                self.socket_cycle_running = False
                sys.stdout.flush()
            