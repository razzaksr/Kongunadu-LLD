from Task import *
from ZealousBoard import *

myProject = ZealousBoard()
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
