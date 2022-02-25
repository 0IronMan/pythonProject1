"""wafunction to add 2 numbers and return the results """
# def add_(a,b):
#     c=a+b
#     return c
# print(add_(1,b=2))

# def add_(a,b,/,*,c ,d):
#     e=a+b+c+d
#     return e
# print(add_(1,2,c=1,d=2))

"""wa function which returns list of even number """
# def even(start,end):
#     l = []
#     for i in range(start,end):
#         if i%2 == 0:
#             l.append(i)
#     return l

# print(even(1,21))
# def fibbo (n):
#     a= 0
#     b = 1
#     i = 0
#     while i < n:
#         print(a)
#         c = a+b
#         a = b
#         b = c
#         i += 1
# fibbo(20)
# print(fibbo(10))


"""wafunction that returns the number o f postion arguments given to the function"""
#
# def spam(*arguments):
#     count = 0
#     for _ in arguments:
#         count += 1
#
#         return count
#
# print(spam(1,2,3,4))
"""retrurn to all the interger values"""

#
# def int_data(*args):
#     for item in args:
#         if isinstance(item,int):
#             print(item)

# int_data(1,2,3,"hai", 19,47, 1+0)

"""wafunction the reverse string"""

# def str_data(*args):
#     for item in args:
#         if isinstance(item, str):
#             print(item[::-1])


# str_data(1, 2, 4.6, 'simple', 'hey', 'cool')


""" variable kewyword arguments """


def keyword_args(**kwargs):
    return kwargs


# print(keyword_args(a=1, b=2, c=3, d=4)

"""no of positional and keyword"""


def count_(*args, **kwargs):
    return len(args), len(kwargs)


print(count_(1, 2, 3, a=10, b=20, c=30))

"""wafunction if the given number of arguments is greater than 5 or not"""


def lenfunction_(*arg):
    if len(arg) > 5:
        return "number of args>5"
    else:
        return "number of args<5"


print(lenfunction_(9, 8, 5, 2))
