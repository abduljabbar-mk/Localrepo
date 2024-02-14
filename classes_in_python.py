class employees:
    
    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email
        
    def greet_person(self):
        print("Hello Welcome to Visual Management " +self.fname)
    
# emp1 = employees('Abdul', 'Jabbar', 'abdul.jabbar@vsmanagement.com')
# emp2 = employees('Muskan', 'Khazi', 'muskan.khazi@vsmanagement.com')

# print(emp1.fname)
# print(emp2.fname)

# emp1.greet_person()
# emp2.greet_person()

class student(employees):
    pass

s=student('Abdul', 'Jabbar','email')
s.greet_person()