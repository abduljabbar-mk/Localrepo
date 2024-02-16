# print('This is the start poin')
# try:
#     print(10/0)
# except:
#     print('Exception occured')
# print('Program Completed')


try:
    num1, num2 = 30,0
    result = num1/num2
    print("Result is", result)
except ZeroDivisionError:
    print('Zero Divison error occured')
except SyntaxError:
    print('Syntax error')
except:
    print('Exception handled....')
else:
    print('No Exception Occured....')
finally:
    print('Executed successfully')
    