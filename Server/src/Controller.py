class GuiController:
    
    def __init__(self, socket):
        self.socket = socket
        
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
        
    # Receive actions from Gui and do things
    
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
        
        
    def configure(self, params):
        print("[RunControl][configure] Configure action begin")
        print("Server received parameters")
        print(self.currentState)
        print(params)
        # can we go configured?
        if "Configure" in self.routes[self.currentState] :
            try:
                print("Configured ... ")
                self.currentState = "Configure"
                self.lastMessage = "Configure ..."
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
            try:
                print("Run ... ")
                self.currentState = "Run"
                self.lastMessage = "Run ..."
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
            try:
                print("Stop ... ")
                self.currentState = "Stop"
                self.lastMessage = "Stop ..."
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
        