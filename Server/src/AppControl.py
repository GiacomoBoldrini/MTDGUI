import os 
import sys 
import subprocess
from datetime import datetime
from .Template import TemplateThreadApp
import threading
import time

class AppController:
    
    def __init__(self, socket):
        self.socket = socket
        self.service = {}
        self.dataApplications = {}
        self.recoApplications = {}
        self.pids = {}
        self.appObj = {}
        
        #you can go up by 1 in this list, or in error, or in any step below (to rerun steps)
        #whose execution was successful
        self.states = {
            "Initialize": 1 ,
            "Configure": 2 ,
            "Data": 3,
            #"Convert": 4,
            "Step1": 4,
            "Step2": 5,
            "Step3": 6,
            "Error": 7,
        }

        self.currentState = "Initialize"


    #needed in case you want to run again some recontrusction or such 
    def externalSetFSMstatus(self, status):
        self.currentState = status 
        return 
    
    def execute(self, key, commands):
        process = subprocess.Popen(commands["exe"], shell=True)
        pid = process.pid
        self.pids[commands["name"]] = pid
        print("prima ti time")
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("prima dell emit")

        self.socket.emit('currentApp', {"app": {"name":commands["name"], "step":key, "time":time, "pid":pid }})
        print("dopo emit")
        out, err = process.communicate()

        if err: print(err)

        return process.returncode

    def canGo(self, finalState):
        if self.states[self.currentState] == self.states[finalState] -1 or self.states[finalState] < self.states[self.currentState]:
            return 1
        else: return 0

    def killAll(self):
        for pid in self.pids: os.system("kill {}".format(pid))
        return 1

    def checkAppExist(self):
        dataOk = 1
        recoOk = 1
        for appName in self.dataApplications.keys():
            appPath = self.dataApplications[appName]["exe"].split(" ")[0]
            if "./" in appPath[:2] : appPath = appPath[2:]
            if "source " in appPath : appPath = appPath.split("source ")[1]
            if "bash " in appPath : appPath = appPath.split("bash ")[1]
            if "python " in appPath : appPath = appPath.split("python ")[1]
            print("---------------------------")
            print("---------------------------")
            #check file existance
            if not os.path.isfile(appPath): 
                dataOk = 0
                print("ERROR: data taking application {} not found in file system".format(appPath))

        for appName in self.recoApplications.keys():
            appPath = self.recoApplications[appName]["exe"].split(" ")[0]
            if "./" in appPath[:2] : appPath = appPath[2:]
            if "./" in appPath[:2] : appPath = appPath[2:]
            if "source " in appPath : appPath = appPath.split("source ")[1]
            if "bash " in appPath : appPath = appPath.split("bash ")[1]
            if "python " in appPath : appPath = appPath.split("python ")[1]
            #check file existance
            if not os.path.isfile(appPath): 
                recoOk = 0
                print("ERROR: reco step application {} not found in file system".format(appPath))

        return dataOk, recoOk


    def parseService(self, sconfig_):
        #will be passed as a json string
        to_gui = []
        sconfig = eval(sconfig_)
        parsingOk = 1
        #checking fields
        mandatory_keys = ["data", "reco"]
        if not all(i in sconfig.keys() for i in mandatory_keys):
            #throw error
            print("ERROR, not matching keys")
            return 0
        for key in sconfig["data"].keys():
            if key not in self.states:
                print("[AppControl][Error] App key {} does not match self.states, check the input ... ".format(key))
                return 0
            appName = sconfig["data"][key].split(" ")[0].split("/")[-1]
            to_gui.append({"step": key, "name": appName, "time": 0, "pid": 0})
            self.dataApplications[key] = {"exe": sconfig["data"][key], "name": appName}
        for key in sconfig["reco"].keys():
            if key not in self.states:
                print("[AppControl][Error] App key {} does not match self.states, check the input ... ".format(key))
                return 0
            appName = sconfig["reco"][key].split(" ")[0].split("/")[-1]
            to_gui.append({"step": key, "name": appName, "time": 0, "pid": 0})
            self.recoApplications[key] = {"exe": sconfig["reco"][key], "name": appName}

        #need a smarter way to check app existance 
        #dataOk, recoOk = self.checkAppExist()
        dataOk, recoOk = 1,1 #for now let's suppose everything is ok
        parsingOk = parsingOk and dataOk and recoOk 

        print("[AppControl] All apps have been checked and saved. Ready to run ...")

        self.currentState = "Configure" #no check because to call this method you have to create the obj therefore it is in initialize by construction
        
        print("ciao")
        self.initApps()

        for key in self.dataApplications.keys():
            for i in range(len(to_gui)):
                if to_gui[i]["step"] == key: to_gui[i]["pid"] = self.dataApplications[key]["pid"]

        for key in self.recoApplications.keys():
            for i in range(len(to_gui)):
                if to_gui[i]["step"] == key: to_gui[i]["pid"] = self.recoApplications[key]["pid"]

        self.socket.emit('queryApps', {"apps": to_gui})


        return parsingOk 


    def initApps(self):
        print(list(self.dataApplications.keys()))
        print(os.getpid())
        for dataApp in self.dataApplications.keys():
            self.dataApplications[dataApp]["app"] = TemplateThreadApp(cmd=self.dataApplications[dataApp]["exe"])
            self.dataApplications[dataApp]["pid"] = self.dataApplications[dataApp]["app"].pid
            self.dataApplications[dataApp]["app"].start()

        for recoApp in self.recoApplications.keys():
            self.recoApplications[recoApp]["app"] = TemplateThreadApp(cmd=self.recoApplications[recoApp]["exe"])
            self.recoApplications[recoApp]["pid"] = self.recoApplications[recoApp]["app"].pid
            self.recoApplications[recoApp]["app"].start()


        print("[AppControl] Initialized all Apps ... Ready to run")

        return


    def runAllApps(self):
        
        print("-----------------------")
        print("Begin Run")
        print("-----------------------")
        #running data taking and so on
        for key in self.dataApplications.keys():
            if self.canGo(key):
                self.dataApplications[key]["app"].runApp()
                while self.dataApplications[key]["app"].shouldRun:
                    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    self.socket.emit('runningApp', {"name": self.dataApplications[key]["name"], "step": key, "pid": self.dataApplications[key]["app"].pid, "time": time})
                    self.socket.sleep(1)
                #here the app finished 
                print("[AppControl] App finished running, updating status")
                self.currentState = key
            else:
                print("[AppControl] Info: Skipping app {}".format(key))

        print("[AppControl] Info: data taking ended successfully")

        for key in self.recoApplications.keys():
            if self.canGo(key):
                self.recoApplications[key]["app"].runApp()
                while self.recoApplications[key]["app"].shouldRun:
                    time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    self.socket.emit('runningApp', {"name": self.recoApplications[key]["name"], "step": key, "pid": self.recoApplications[key]["app"].pid, "time": time})
                    self.socket.sleep(1)
                #here the app finished 
                print("[AppControl] App finished running, updating status")
                self.currentState = key
            else:
                print("[AppControl] Info: Skipping app {}".format(key))


        #returnin a nice message if everything is ok
        #print("final: ", self.currentState)
        #return 1, self.currentState


    def threadRun(self):

        tf = threading.Thread(target=self.runAllApps)
        tf.start()
        print("Waiting for thread to end")
        tf.join() 

        return 1, "Step3"
