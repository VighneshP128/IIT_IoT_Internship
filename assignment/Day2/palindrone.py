num1=int(input("Enter number="))
rev=0
original=num1
while num1>0:
    digit=num1%10
    rev=rev*10+digit
    num1//=10
print("reverse number:",rev)
if original==rev:
       print("Number is palindrone")
else:
 print("Number is not palindrone")