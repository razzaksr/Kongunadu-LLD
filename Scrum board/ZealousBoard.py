from Task import *
from dotenv import *
import os
from pymongo import *
import json

class ZealousBoard:
    '''data with CRUD'''
    buckets={
        "todo":[],"progress":[],"review":[],"done":[]
    }
    # CRUD operations: create task, update task, delete task, read task
    def __init__(self):
        load_dotenv()
        self.uri = "mongodb+srv://"+os.getenv('user')+":"+os.getenv('password')+"@cluster0.ptmlylq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = MongoClient(self.uri)
        self.db = self.client.kongunadu
        self.collection = self.db.task
    def load(self):
        self.buckets={
            "todo":[],"progress":[],"review":[],"done":[]
        }
        bsons = self.collection.find()
        for bson in bsons:
            # json to object
            # print(bson)
            task = Task(bson['taskId'],bson['taskName'],bson['taskAssigner'],bson['taskAssignee'],bson['taskStoryPoints'],bson['taskBucket'])
            if task.taskBucket == 'todo':
                self.buckets['todo'].append(task)
            elif task.taskBucket == 'progress':
                self.buckets['progress'].append(task)
            elif task.taskBucket == 'review':
                self.buckets['review'].append(task)
            elif task.taskBucket == 'done':
                self.buckets['done'].append(task)
    
    def viewBoard(self):
        # read all from mongodb
        self.load()
        for bucket in self.buckets.keys():
            print(bucket,"bucket task's of ")
            for x in self.buckets[bucket]:
                    print(str(x))
        
    
    # adding task to bucket>> Create
    def addToBucket(self,task,bucket):
        jsonTask = {
            "taskId":task.taskId,
            "taskName":task.taskName,
            "taskAssigner":task.taskAssigner,
            "taskAssignee":task.taskAssignee,
            "taskStoryPoints":task.taskStoryPoints,
            "taskBucket":task.taskBucket
        }
        # print(jsonTask)
        if bucket == 'todo':
            self.collection.insert_one(jsonTask);
        else:
            self.collection.update_one({"taskId":task.taskId},{"$set":jsonTask})
        print(task.taskId," included in the ",bucket)
        # if bucket == 'todo' and task.taskBucket=='todo':
        #     # self.buckets['todo'].append(task)
        #     jsonTask = json.dump(task)
        #     self.collection.insert_one(jsonTask);
        #     print(task.taskId," included in the ",bucket)
        # elif bucket == "progress" and task.taskBucket =="progress":
        #     for x in range(len(self.buckets['todo'])):
        #         if self.buckets['todo'][x].taskId==task.taskId:
        #             # print("To be removed ",str(self.buckets['todo'][x]))
        #             self.buckets['todo'].remove(self.buckets['todo'][x])
        #             self.buckets['progress'].append(task)
        #             print(task.taskId," has been moved to "+task.taskBucket)
        #             return
        #     else:
        #         print('Invalid task/bucket')
        # elif bucket == "review" and task.taskBucket =="review":
        #     for x in range(len(self.buckets['progress'])):
        #         if self.buckets['progress'][x].taskId==task.taskId:
        #             # print("To be removed ",str(self.buckets['progress'][x]))
        #             self.buckets['progress'].remove(self.buckets['progress'][x])
        #             self.buckets['review'].append(task)
        #             print(task.taskId," has been moved to "+task.taskBucket)
        #             return
        #     else:
        #         print('Invalid task/bucket')
        # elif bucket == "done" and task.taskBucket =="done":
        #     for x in range(len(self.buckets['review'])):
        #         if self.buckets['review'][x].taskId==task.taskId:
        #             # print("To be removed ",str(self.buckets['review'][x]))
        #             self.buckets['review'].remove(self.buckets['review'][x])
        #             self.buckets['done'].append(task)
        #             print(task.taskId," has been moved to "+task.taskBucket)
        #             return
        #     else:
        #         print('Invalid task/bucket')
            
    
    def readFromBucket(self,bucket):
        #print(bucket)
        self.load()
        if bucket == 'todo' or bucket == 'progress' or bucket == 'review' or bucket == 'done':
            print("The task in the "+bucket+" buckets are")
            for x in self.buckets[bucket]:
                print(str(x))
        else:
            print("invalid bucket")
    
    def readByEmployee(self,name):
        self.load()
        for bucket in self.buckets.keys():
            print(bucket,"bucket task's of ",name)
            for x in self.buckets[bucket]:
                if x.taskAssignee == name:
                    print(str(x))