# class MyClass:
#     name = "Abdul"
#     def __init__(self,name):
#         print(name)
#         print(self.name)
        

# mc = MyClass("Jabbar")

##########################################

#Requirement
#Class : Employees, 
# Contructor : eid, ename, salary
# method : (Display): eid, ename & sal

# class Employees:
#     def __init__(self, eid, ename, salary):
#         self.eid = eid                           #(self.eid = eid) This will Convert the local varible to class variable.
#         self.ename = ename
#         self.salary = salary
    
#     def display(self):
#         print(self.eid, self.ename, self.salary)
    
# e1 = Employees(101, 'Abdul Jabbar', 5000000)
# e1.display()

# e2 = Employees(102, 'Shoaib', 7000000)
# e2.display()

class Employees:
    def __init__(self, eid, ename, salary):
        self.eid = eid                           #(self.eid = eid) This will Convert the local varible to class variable.
        self.ename = ename
        self.salary = salary
    
    def __str__(self):
        return(self.ename)
    
e1 =Employees(101,"Abdul",5000000)
print(e1)      