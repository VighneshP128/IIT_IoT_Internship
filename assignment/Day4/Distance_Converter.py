d=int(input("Enter Distance="))
def Distance_Converter(d):
    m=d*1000  #km-m
    print("Km to m=",m)
    cm=m*100
    print("m to cm=",cm)
    mm=cm*10
    print("cm to mm=",mm)
    f=m*3.280
    print("m to f=",f)
    i=f*12
    print("f to i=",i)
    c=i*2.54
    print("i to cm=",c)

def Print_Result():
      Distance_Converter(d)
      
    
Print_Result()