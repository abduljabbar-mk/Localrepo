# class employees:
    
#     def __init__(self, fname, lname, email):
#         self.fname = fname
#         self.lname = lname
#         self.email = email
        
#     def greet_person(self):
#         print("Hello Welcome to Visual Management " +self.fname)
    
# emp1 = employees('Abdul', 'Jabbar', 'abdul.jabbar@vsmanagement.com')
# emp2 = employees('Muskan', 'Khazi', 'muskan.khazi@vsmanagement.com')

# print(emp1.fname)
# print(emp2.fname)

# emp1.greet_person()
# emp2.greet_person()

# class student(employees):
#     pass

# s=student('Abdul', 'Jabbar','email')
# s.greet_person()

# class MyClass:
#     def myfun(self):
#         pass
#     def display(self, name):
#         print(name)

# c=MyClass()
# c.myfun()
# c.display('Abdul')

class annotationsClass:
    def new1(self):
        print('This is a instance class')
    
    @staticmethod
    def stat_method(self, num):
        print(self, num)

new=annotationsClass()
new.new1()

new.stat_method(50,10)

annotationsClass.stat_method(10,20) 