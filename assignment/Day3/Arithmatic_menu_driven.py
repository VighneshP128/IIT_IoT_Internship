num1=int(input("Enter Number"))
num2=int(input("Enter Number"))

print("1. Addition")
print("2. substraction")
print("3. multiplication")
print("4. division")

def addition(num1,num2):
   print("Addition=",num1+num2)
def substraction(num1,num2):
   print("substraction=",num1-num2)
def multiplication(num1,num2):
   print("multiplication=",num1*num2)
def division(num1,num2):
  print("division=",num1/num2)

choice=int(input("Enter Choice="))

match choice:
 case 1:
    addition(num1,num2)
 
 case 2:
   substraction(num1,num2)

 case 3:
   multiplication(num1,num2)

 case 4:
   division(num1,num2)

