import threading 
import time 
import os
import subprocess

class TemplateThreadApp(threading.Thread):

    def __init__(self, cmd=None):

        super(TemplateThreadApp, self).__init__()
        self.cmd = cmd 

        self.shouldRun = False
        self.pid = os.getpid()

    def run(self):
        
        while not self.shouldRun:
            # infinite loop while wating to proceed
            continue

        print("Hey! Sto girando ora")

        print("Running {}".format(self.cmd))

        process = subprocess.Popen(self.cmd.split()) # runs
        self.pid = process.pid #retrieves pid
        print("Il pid della nuova app che ho lanciato: {}".format(process.pid))
        process.wait() # wait until this step is completed
        print("Ciao scemo sono gia qui")
        self.shouldRun = False # at this point the comand should be completed
        return 


    def runApp(self):
        self.shouldRun = True
        return 