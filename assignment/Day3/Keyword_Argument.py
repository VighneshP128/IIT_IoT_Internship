def info(name="student"):
    print("Hello,", name)


info("vighnesh")
info()  


def student_info(name, age, ID):
    print("Name:", name)
    print("Age:", age)
    print("Course ID:", ID)


student_info(name="vighnesh",age=21,ID=66)


def add(a, b):
    return a + b

def operate(func, x, y):
    return func(x, y)


result = operate(add, 5, 3)
print("Result:", result)