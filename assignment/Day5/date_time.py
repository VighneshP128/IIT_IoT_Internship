import datetime 
now=datetime.datetime.now()

print("day=",now.strftime("%A"))
print("date=",now.strftime("%d-%m-%y"))
print("time=",now.strftime("%H-%M-%S"))