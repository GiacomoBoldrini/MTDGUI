import threading 
import time 
import os
import signal
import subprocess

class TemplateThreadApp(threading.Thread):

    def __init__(self, cmd=None):

        super(TemplateThreadApp, self).__init__()
        self.cmd = cmd 

        self.run_event = threading.Event()
        self.pid = os.getpid()

    def run(self):
        
        self.run_event.wait() #wait until the event is set 

        #while self.run_event.is_set():

        print("Hey! Sto girando ora")

        print("Running {}".format(self.cmd))

        commands_tl = self.cmd.split(" && ")
        print(commands_tl)

        for command in commands_tl:
            if not self.run_event.is_set(): 
                print("TI ROMPO TUTTO :)")
                break
            print("Running: {}".format(command))
            #horrible
            if "cd" in command:
                cmd_tmp = command[3:]
                os.chdir(cmd_tmp)
            elif "source" in command or "/bin/sh" in command: 
                os.system(command)
            else:
                self.process = subprocess.Popen(command.split()) # runs
                self.pid = self.process.pid #retrieves pid
                print("Il pid della nuova app che ho lanciato: {}".format(self.process.pid))
                self.process.wait() # wait until this step is completed

                self.successful = not self.process.returncode #return 0 is succesfull, 1 not successfull so invert logic
                #self.successful = True
                if not self.successful:
                    print("[Template] Running  NOT ok... breaking")
                    break #do not run any more 

            print("Running went ok...")

        self.run_event.clear() # at this point the comand should be completed
        return 


    def runApp(self):
        self.run_event.set() 
        return 

    def stopApp(self):
        self.run_event.clear()
        os.kill(self.pid, signal.SIGINT)

        return

    def isRunning(self):
        return self.run_event.is_set()