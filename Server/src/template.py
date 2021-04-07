# AT THE MOMENT THIS IS A COPY OF the templateApp.py from ECAL DAQ
# Cucciati et. al.
# https://gitlab.cern.ch/ecal-daq-upgrade/H4WEBGUI/-/blob/master/Server/src/templateApp.py

from fsm import FSM
import threading
import argparse
from bs4 import BeautifulSoup as Soup

class theApp(FSM):
    """
        A custom app inheriting from an FSM.
        No Init as we need the FSM constructor.
    """
    
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-c", "--configurefile", type=str, help="Configuration file", required=True)
    # parser.add_argument("-l", "--logfile", type=str, help="Log file", required=True)
    # args = parser.parse_args()
    # self.configure_file_path = args.configurefile
    # self.log_file_path = args.logfile


    def parse_standard_params(self):
        # We parse the config file to extracts port numbers.
        print("Looking for ports...")
        # port_list = []
        # for tag in soup.find_all("ListenPort"):
        #     port_list.append(tag.string)
        # self.data_port = port_list[0]
        # self.status_port = port_list[1]
        # self.cmd_port = port_list[2]
        self.data_port = 7010
        self.status_port = 7012
        self.cmd_port = 7014
        print("Data port: ",self.data_port," - Status port: ",self.status_port," - Cmd port: ",self.cmd_port)

        # Url list for ZMQ to subscribe to:
        # for tag in soup.find_all("ConnectTo"):
            # self.sub_urls.append(tag.string)
        self.sub_urls.append(['Giacomo:5567', 'Giacomo:5566'])

    # In this function you can extract other parameters from the config file
    def parse_custom_params(self):
        print("Parsing custom params...")
        # Write here

    def parse_configure_file(self):
        try:
            # print("Configure file path sent by AppControl: ",self.configure_file_path)
            print("Configure")
            # with open(self.configure_file_path) as fp:
            #    soup = Soup(fp, "xml")
            self.parse_standard_params()
            self.parse_custom_params()
        
        except:
            raise Exception("parse_configure_file failed")

    # Function used by the thread
    def thread_function(self):
        counter = 0
        while self.runningFlag:
            if self.status == 'INITIALIZED':
                print('Do something when INITIALIZED...')
            if self.status == 'CLEARED':
                print('Do something when CLEARED...')
            for i in range(10):
                time.sleep(1)
                if not self.runningFlag:
                    break
    
    def proc_message(self, msg):
        # here you can check the command string and launch the 
        # correspondent callback like the following KILL_APP.
        # Keep KILL_APP if you want the closing of the application controlled by the GUI (suggested)
        print('Message from subscription:', msg)
        if 'GUI_STARTRUN' in msg:
            self.start()
        if 'KILL_APP' in msg:
            self.exit()
        if 'GUI_STOPRUN' in msg:
            self.stop()
        if 'BLABLABLA' in msg:
            print('A new command...')
        
    def initialize(self):
        print("initialize action begin")
        self.parse_configure_file()
        self.initialize_zmq_channels()
        self.socket_cycle_running = True
        self.currentState = 'Configure'

        # Thread for periodic actions
        self.runningFlag = True
        self.theThread = threading.Thread(target=self.thread_function, args=())
        self.theThread.start()
        print("initialize action end")

    def configure(self):
        print("configure action begin")
        print("configure action end")

    def start(self):
        print("start action begin")
        self.status = 'CLEARED'
        print("start action end")

    def stop(self):
        print("stop action begin")
        self.status = 'INITIALIZED'
        print("stop action end")

    def pause(self):
        print("pause action begin")
        print("pause action end")

    def resume(self):
        print("resume action begin")
        print("resume action end")

    def fail(self):
        print("fail action begin")
        self.socket_cycle_running = False
        print("fail action end")

    def reset(self):
        print("reset action begin")
        print("reset action end")

    def exit(self):
        print("exit action begin")
        self.socket_cycle_running = False
        self.runningFlag = False
        self.status = 'BYE'
        print("exit action end")

        
        
### Main ###

if __name__ == "__main__":

    newApp = theApp()
    print(newApp.data_port)
    newApp.initialize()
    newApp.listen_socket()
