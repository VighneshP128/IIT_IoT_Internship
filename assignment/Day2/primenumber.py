def prime(a,num1):
  
 if num1<=1:
  a=0
 else:
      for i in range(2,num1):
            if num1%i==0:
                  a=0
 if a==1:
        print("number is prime")
        
 else:
        print("number is not prime")

num1=int(input("Enter Number="))
a=1
prime(a,num1)
