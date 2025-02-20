from Task import *
from ZealousBoard import *

myProject = ZealousBoard()

print("welcome to Zealous Board for your Project Management")

while(True):
    print("1.Manage Task\n2.View Board\n3.View Bucket\n4.View by employee\nAny to logout")
    choice = int(input("Enter your choice "))
    if choice == 1:
        print("enter task details such as ")
        task = Task(
            int(input("Enter your task id ")),
            input("Enter the task name "),
            input("Enter your name of scrum master "),
            input("Enter the name to assign "),
            int(input("Enter your story points ")),
            input("Enter name of the bucket ")
            )
        myProject.addToBucket(task,task.taskBucket)
    elif choice == 2:myProject.viewBoard()
    elif choice == 3:
        myProject.readFromBucket(input("tell us name of the bucket to read "))
    elif choice == 4:
        myProject.readByEmployee(input("tell us name of the employee to show the board "))
    else:
        break



'''
# task creation
task1 = Task(12,"Build Login Page","Razak Mohamed S","Praveen",24,"todo")
task2 = Task(105,"Generate ER diagram","Razak Mohamed S","Noorul",5,"todo")
task3 = Task(98,"Perform Integration testing","Vinayak","Praveen",2,"todo")
task4 = Task(102,"Perform CI/CD","Razak Mohamed S","Balaji",8,"todo")
# task insertion into bucket>> create
myProject.addToBucket(task1,'todo')
myProject.addToBucket(task2,'todo')
myProject.addToBucket(task3,'todo')
myProject.addToBucket(task4,'todo')
# read 
# myProject.readFromBucket("todo")
# 
task1 = Task(12,"Build Login Page","Razak Mohamed S","Praveen",24,"progress")
myProject.addToBucket(task1,"progress")
# myProject.readFromBucket("todo")
# myProject.readFromBucket("progress")
task1 = Task(12,"Build Login Page","Razak Mohamed S","Praveen",24,"review")
myProject.addToBucket(task1,"review")
# myProject.readFromBucket("progress")
# myProject.readFromBucket("review")
task1 = Task(12,"Build Login Page","Razak Mohamed S","Praveen",24,"done")
myProject.addToBucket(task1,"done")
# myProject.readFromBucket("review")
# myProject.readFromBucket("done")


# myProject.readByEmployee('Praveen')
myProject.readByEmployee('Balaji')
'''