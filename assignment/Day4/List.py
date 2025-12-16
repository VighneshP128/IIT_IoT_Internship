l1=[11,22,33,44,55]
l2=[22,33,34,44,98]

def overlapping():
    index=0
    c=1
    for index in range(len(l1)-1):
         for index in range (len(l2)):
              if l1[index]==l2[index]:
                c+=c
              else:
                c=c
              l2[index]+=l2[index]
         l1[index]+=l1[index]
    
    if c>=1:
        print("true",c)  
    else:
        print("false")   

overlapping()
