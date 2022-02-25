# def spam(func):
#     def wrapper(*args, **kwargs):
#         print("the no of arguments are :",len(args) + len(kwargs))
#         func(*args, **kwargs)
#     return wrapper
#
# @spam        # add = spam(add)
# def add(a, b):
#     print(a + b)
# # add(1, 2)
#
#
#
# import time
#
# def delay(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(2)
#         return func(*args, **kwargs)
#     return wrapper
#
# @delay
# def display():
#     return "in display"
# print(display())
#
# def reverse(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)[::-1]
#     return wrapper
#
# @reverse
# def input_(a):
#     return a
#
# print(input_("hello"))
#
# '''wadecorater to execute a function for three time'''
# def outer_(n):
#     def repeate_(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#               return func(*args, **kwargs)
#         return wrapper
#
# @repeate_
# def add(a, b):
#     print(a - b)
#

# import time
#
# def outer_(n):
#     def delay(func):
#         def wrapper(*args,  **kwargs):
#             time.sleep(n)
#             func(*args, **kwargs)
#         return wrapper
#     return delay
#
# @outer_(3)
# def add_(a,b):
#     print(a + b)
#
# @outer_(2)
# def sub(a, b):
#     print(a - b)
# 
# sub(10,8)
# add_



'''wadecorater function to the count the number of arguments passed to a function'''

#
# def count_(func):
#     def wrapper(*args, **kwargs):
#         print(f"count arguments{len(args) +len(kwargs)}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @count_ # display = count_(display)
# def display_(*args):
#     return args
#
# print(display_(12663))

#
# def factorial_(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial_(n-1)
# n = int(input("enter the n vale"))
# res = factorial_(n)
# print(res)

# def spam(func):
#     def wrapper(*args, **kwargs):
#         print("i love u")
#         return func(*args, **kwargs)
#     return wrapper
#
# @spam
# def cool(a, b):
#     print(f"krishna miss u so much: {a + b}")
#
# cool(140, 3)
#
# def logging(msg="hello world", debug=True):
#     def log(func):
#         def wrapper(*args, **kwargs):
#             if debug:
#                 print(msg, func.__name__)
#             return func(*args, **kwargs)
#         return wrapper
#     return log

