from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

class DBMan:
    
    def __init__(self):
        
        self.client = MongoClient("localhost", 27017)
        self.db = self.client.mtddb
        self.app_configs = self.db.app_configs
        self.service_configs = self.db.service_configs
        self.run_config = self.db.run_configs
        self.run_registry = self.db.run_registry

    # ------ Service Keys --------

    def GetAllServices(self):
        # cursor to select everything from the service collection
        theServiceList = list(self.service_configs.find())
        print(dumps(theServiceList))
        return dumps(theServiceList)

    def PostService(self, data):
        # cursor to select everything from the service collection
        try:
            self.service_configs.insert_one(data)
            return 1
        except:
            return 0

    def DeleteService(self, _id):
        # cursor to select everything from the service collection
        try:
            result = self.service_configs.delete_one({'_id': ObjectId(_id['$oid'])})
            print(result)
            return 1
        except:
            return 0

    def PutService(self, obj):
        _id = obj['_id']['$oid']
        name = obj['name']
        config = obj['config']
        print(_id,  name, config)
        # cursor to select everything from the service collection
        try:
            result = self.service_configs.update_one({'_id': ObjectId(_id)}, { "$set": {"name": name, "request_config": config}})
            return 1
        except:
            return 0


    # ------ Run Keys --------


    def GetAllRuns(self):
        # cursor to select everything from the service collection
        theServiceList = list(self.run_config.find())
        print(dumps(theServiceList))
        return dumps(theServiceList)

    def PostRun(self, data):
        # cursor to select everything from the service collection
        try:
            self.run_config.insert_one(data)
            return 1
        except:
            return 0

    def DeleteRun(self, _id):
        # cursor to select everything from the service collection
        try:
            result = self.run_config.delete_one({'_id': ObjectId(_id['$oid'])})
            print(result)
            return 1
        except:
            return 0

    def PutRun(self, obj):
        _id = obj['_id']['$oid']
        name = obj['name']
        config = obj['config']
        print(_id,  name, config)
        # cursor to select everything from the service collection
        try:
            result = self.run_config.update_one({'_id': ObjectId(_id)}, { "$set": {"name": name, "request_config": config}})
            return 1
        except:
            return 0
        
        
    # ------ Run Registry --------


    def GetRunReg(self):
        # cursor to select everything from the service collection
        theRunList = list(self.run_registry.find())
        print(dumps(theRunList))
        return dumps(theRunList)

    def PostRunReg(self, data):
        # cursor to select everything from the service collection
        result = self.run_registry.insert_one(data)
        print(result.inserted_id)
        return 1