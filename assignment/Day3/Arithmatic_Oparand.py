num1=int(input("Enter Number"))
num2=int(input("Enter Number"))

def calculate():
  addition(num1,num2)
  substraction(num1,num2)
  multiplication(num1,num2)
  division(num1,num2)
 
def addition(num1,num2):
   print("Addition=",num1+num2)
def substraction(num1,num2):
   print("substraction=",num1-num2)
def multiplication(num1,num2):
   print("multiplication=",num1*num2)
def division(num1,num2):
  print("division=",num1/num2)

calculate()


