def histogram():
    d="*"
    print("histogram(a,b,c)")
    a=int(input("Enter a="))
    b=int(input("Enter b="))
    c=int(input("Enter c="))
    while a>0:
     print(d,end="")
     a-=1
    print("")
    while b>0:
      print(d,end="")
      b-=1
    print("")  
    while c>0:
     print(d,end="")
     c-=1
    print("")

histogram()

