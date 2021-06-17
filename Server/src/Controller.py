from .DBManager import DBMan
from .AppControl import AppController
import datetime

class GuiController:
    
    def __init__(self, socket, dbman):
        self.socket = socket
        self.AppC = AppController(socket)
        self.dbman = dbman
        self.currentState = "None"
        self.msg = ""
        self.states = {
            "None": 0,
            "Initialize": 1 ,
            "Configure": 2 ,
            "Run": 3 ,
            "Pause": 4 ,
            "Resume": 5 ,
            "Stop": 6,
            "Error": 7,
        }
        self.routes = {
            "None": ["Initialize", "Error"],
            "Initialize": ["Configure", "Error"],
            "Configure": ["Run", "Error"],
            "Run": ["Pause", "Stop", "Error"],
            "Pause": ["Resume", "Stop", "Error"],
            "Resume": ["Pause", "Stop", "Error"],
            "Stop": ["Error"],
            "Error": []
        }
        self.run_status = 1  #"run property" is actually composite as it contains every possible action you would like to do
        
    # Receive actions from Gui and do things


    def updateState(self, status):
        self.socket.emit('updateTheState', {"state": status})
        return
    
    def initialize(self):
        print("[RunControl][initialize] Initialize action begin")
        # can we go ininitialize?
        if "Initialize" in self.routes[self.currentState] :
            try:
                print("Initialized ... ")
                self.currentState = "Initialize"
                self.lastMessage = "Initialized ..."
                return self.states[self.currentState], self.lastMessage
                # do somthing...
            except:
                if "Error" in self.routes[self.currentState] :
                    self.currentState = "Error"
                    self.lastMessage = "An error appeared while initializing"
                    return self.states[self.currentState], self.lastMessage
                else:
                    raise Exception("Error")

        else:
            self.lastMessage = "Transition not allowed!"
            return self.states[self.currentState], self.lastMessage
        
        
    def configure(self, config):
        print("[RunControl][configure] Configure action begin")
        print("Server received parameters")
        service = config["service"]
        runkey = config["runkey"]
        service.pop("_id", None)
        runkey.pop("_id", None)
        # can we go configured?
        if "Configure" in self.routes[self.currentState] :
            try:
                print("Configured ... ")
                self.currentState = "Configure"
                self.lastMessage = "Configure ..."
                self.configuration = {"service": service, "runkey": runkey}
                #initializing apps in appcontrol
                status = self.AppC.parseService(service["request_config"])
                if not status:
                    if "Error" in self.routes[self.currentState] :
                        self.currentState = "Error"
                        self.lastMessage = "An error appeared while Configure"

                return self.states[self.currentState], self.lastMessage
                # do somthing...
            except:
                if "Error" in self.routes[self.currentState] :
                    self.currentState = "Error"
                    self.lastMessage = "An error appeared while Configure"
                    return self.states[self.currentState], self.lastMessage
                else:
                    raise Exception("Error")

        else:
            self.lastMessage = "Transition not allowed!"
            return self.states[self.currentState], self.lastMessage
        
    def start(self):
        print("[RunControl][initialize] Run action begin")
        # can we go ininitialize?
        if "Run" in self.routes[self.currentState] :
            self.currentState = "Run"
            self.lastMessage = "Run ..."
            self.updateState(self.states[self.currentState])

            """
            try:
                self.stop()
            except:
                pass

            return self.states[self.currentState], self.lastMessage

            """
            #try:
            execution, run_status = self.AppC.threadRun()
            self.run_status = run_status
            #after execution we can set the state to stop if successfull
            self.stop()
            if not execution:
                self.currentState = "Error"
                self.lastMessage = "An error appeared while Run"

            return self.states[self.currentState], self.lastMessage
            # do somthing...
            # except:
            #     if "Error" in self.routes[self.currentState] :
            #         self.currentState = "Error"
            #         self.lastMessage = "An error appeared while Run"
            #         return self.states[self.currentState], self.lastMessage
            #     else:
            #         raise Exception("Error")
            

        else:
            self.lastMessage = "Transition not allowed!"
            return self.states[self.currentState], self.lastMessage
        
        
    def pause(self):
        print("[RunControl][pause] Pause action begin")
        # can we go ininitialize?
        if "Pause" in self.routes[self.currentState] :
            try:
                print("Pause ... ")
                self.currentState = "Pause"
                self.lastMessage = "Pause ..."
                return self.states[self.currentState], self.lastMessage
                # do somthing...
            except:
                if "Error" in self.routes[self.currentState] :
                    self.currentState = "Error"
                    self.lastMessage = "An error appeared while Run"
                    return self.states[self.currentState], self.lastMessage
                else:
                    raise Exception("Error")

        else:
            self.lastMessage = "Transition not allowed!"
            return self.states[self.currentState], self.lastMessage
        
    def resume(self):
        print("[RunControl][resume] Resume action begin")
        # can we go ininitialize?
        if "Resume" in self.routes[self.currentState] :
            try:
                print("Resume ... ")
                self.currentState = "Resume"
                self.lastMessage = "Resume ..."
                return self.states[self.currentState], self.lastMessage
                # do somthing...
            except:
                if "Error" in self.routes[self.currentState] :
                    self.currentState = "Error"
                    self.lastMessage = "An error appeared while Run"
                    return self.states[self.currentState], self.lastMessage
                else:
                    raise Exception("Error")

        else:
            self.lastMessage = "Transition not allowed!"
            return self.states[self.currentState], self.lastMessage
        
    def stop(self):
        print("[RunControl][pause] Stop action begin")
        # can we go ininitialize?
        if "Stop" in self.routes[self.currentState] :
            self.currentState = "Stop"
            self.lastMessage = "Stop ..."
            self.updateState(self.states[self.currentState])
            try:
                print("Stop ... ")
                #saving run on db
                self.dbman.PostRunReg({"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "configuration": self.configuration, "status": self.states[self.currentState]})
                return self.states[self.currentState], self.lastMessage
                # do somthing...
            except:
                if "Error" in self.routes[self.currentState] :
                    self.currentState = "Error"
                    self.lastMessage = "An error appeared while Stop"
                    return self.states[self.currentState], self.lastMessage
                else:
                    raise Exception("Error")

        else:
            self.lastMessage = "Transition not allowed!"
            return self.states[self.currentState], self.lastMessage
        
    def restart(self):
        print("[RunControl][restart] Restart action begin")
        self.currentState = "None"
        self.lastMessage = "Restarting the app"
        return self.states[self.currentState], self.lastMessage
    
    
    def error(self):
        print("[RunControl][error] Error action begin")
        # can we go in error? Yes otherwise we are already in error
        if "Error" in self.routes[self.currentState] :
            try:
                print("Error ... ")
                # Post configuration to run  registry before changing state so one knows 
                # At which point an error has been fired
                self.dbman.PostRunReg({"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "configuration": self.configuration, "status": self.states[self.currentState]})
                self.currentState = "Error"
                self.lastMessage = "Error ..."
                return self.states[self.currentState], self.lastMessage
                # do somthing...
            except:
                if "Error" in self.routes[self.currentState] :
                    self.currentState = "Error"
                    self.lastMessage = "An error appeared while error"
                    return self.states[self.currentState], self.lastMessage
                else:
                    raise Exception("Error")

        else:
            self.lastMessage = "Transition not allowed!"
            return self.states[self.currentState], self.lastMessage
        