class Task:
    '''Task class with required attributes'''
    def __init__(self, id=0,name='',manage='',employee='',points=0,bucket=''):
        self.taskId=id
        self.taskName=name
        self.taskAssigner = manage
        self.taskAssignee = employee
        self.taskStoryPoints = points
        self.taskBucket = bucket
    
    def __str__(self):
        return "Task Information: {\n"+"task_Id:"+str(self.taskId)+",\ntask_name:"+self.taskName+",\ntask_assigner:"+self.taskAssigner+",\ntask_assignee:"+self.taskAssignee+",\ncurrent_bucket:"+self.taskBucket+",\nstory_points:"+str(self.taskStoryPoints)+"\n}"

# # contructor
# task1 = Task(12,"Build Login Page","Razak Mohamed S","Praveen",24,"todo")
# # str
# print(task1)