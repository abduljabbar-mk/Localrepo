# Single Level

# class A:
#     def m1(self):
#         print("This is claas A Method")
        
# class B(A):
#     def m2(self):
#         print("This Is Class B Method")
        
# b_obj = B()
# b_obj.m1()
# b_obj.m2()

class A:
    a=int(input("Insert 1st number:", ))
    b=int(input("Insert 2nd Number:", ))
    def m1(self):
        print(self.a+self.b)
        
class B(A):
    def m2(self,x,y):
        print(x,y)
        
obj_b=B()
obj_b.m1()
obj_b.m2
