"""postional arguments """
def greet(name,age):
    print(f"{name} is {age} years old")
#greet(name="ram",age=20)
#greet(age=20, name="ram")


"""combination of keyworand postion """
def add_(a,b,c,d):
    print(a,b,c,d)

# add_(a,b,c,d)
# add_(a=1,b=2,c=3,d=4)
#add_(a=1,b=2. b,c) #syntax
#error

""""postional only arguments"""
def add_(a, b, c, d,/):
    print(a, b, c, d)
add_(1,2,3,4)
#add_(a=1,b=2,c=3,d=4) #error
#
# """keyword only arguments """
def add_(*,a,b,c,d):
    print(a,b,c,d)

# add_(a=1,b=2,c=3,d=4)
# add_(1,2,a=3,b=4) #typeerror

def add_(a, b,*, c, d,):
    print(a, b, c, d)
add_(1,2,c=3,d=4)
#slash represent postional only arguments , if a function defination has slash in the parameter list then the parameters define
#before slash must accept only postional arguments, but parameter after slash can accept either positional or keyword argument
