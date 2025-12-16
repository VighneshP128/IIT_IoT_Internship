d=int(input("Enter Distance="))
m=lambda d:d*1000
cm=lambda m:m*100
mm=lambda cm:cm*10
f=lambda m:m*3.280
i=lambda f:f*12
c=lambda i:i*2.54

def Distance_Converter():
    
    print(f"Killometer to meter={m(d)}")
    
    print(f"meter to centimeter={cm(d)}")
    
    print(f"centimeter to millimeter={mm(d)}")
   
    print(f"meter to feet={f(d)}")

    print(f"feet to inches={i(d)}")

    print(f"inches to centimeter={c(d)}")


Distance_Converter()