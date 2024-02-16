import sys
sys.path.append("Localrepo/packA")
sys.path.append("Localrepo/packB")


#Approach 1
# import emp
# empobj = emp.Employee(101,"Abdul", 450000)
# empobj.displayemp()

# import stu 
# stuobj = stu.Student(1122, "shoaib", 'B')
# stuobj.displaystu()

#Approch 2
from emp import Employee
empobj = Employee(102,"jabbar", 500000)
empobj.displayemp()

from stu import Student
stuobj = Student(1020, "Shaikh", 'A')
stuobj.displaystu()

