n=int(input("Enter number"))
b=int(input("Enter Base"))
e=int(input("Enter Exponential"))
def fact(n):
     
     if n==0 or n==1:
      return 1
     return n * fact(n-1)
def power(b,e):
     
     if e==0:
      return 1
     return b*power(b,e-1)
    
print("factorial",fact(n))
print("power=",power(b,e))


  
