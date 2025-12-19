d=int(input("Enter Distance="))
def Distance_Converter(d):
    m=d*1000  #km-m
    print("Killometer to meter=",m,"m")
    cm=m*100
    print("meter to centemeter=",cm,"cm")
    mm=cm*10
    print("centemeter to millimeter=",mm,"mm")
    f=m*3.280
    print("millimeter to feet=",f)
    i=f*12
    print("feet to inches=",i)
    c=i*2.54
    print("inches to centemeter=",c)

def Print_Result():
      Distance_Converter(d)
      
    
Print_Result()