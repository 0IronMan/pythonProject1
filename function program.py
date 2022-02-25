"""wafunction to give message hi every onhe"""

# def msg_(message=0):
#     if _ in message:
#         i == 0
#         print("hi  everyone")
#
# msg_(0):

"""writr a function whether the number is prime or not"""

# def prime_number(n):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 return f"{n} is not prime number"
#
#         return "n is prime number"


# print(prime_number(13))

"""wafunction name tail that take a sequence as input & a number n and the return the last element from the sequnce"""

# def tail_(sequence, n):
#     return sequence[-n:]
#
#
#
# print(tail_("hello", 2))


"""is perfedt squre"""


def is_perfect_squre(num):

    for i in range(num):
        if i * i == num:
            return True
    return False

#print(is_perfect_squre(34))


""" write a function is number fibonacci or not"""

# def fibonacci_(n):
#     a = 0
#     b = 1
#     i = 0
#     while i <= n:
#          l = []
#          l.append(a)
#          c = a+b
#          a = b
#          b = c
#          i += 1
#          if i in l:
#              return f"{n}is number fibonacci number"
#          return f"{n}is not fibonacci number"
#
#
# print(fibonacci_(5))


# def is_fibo(num):
#     a = 0
#     b = 1
#     while a <= num:
#         if a == num:
#             return f"{num} is a fibonacci number"
#         c = a + b
#         a = b
#         b = c
#     return f"{num}is not a fibonacci number"
#
# print(is_fibo(0))

"""wafunction the take  variable number of inputs and return all the iterable givens"""
#
# def iterable_length(*args):
#     for item in args:
#         if isinstance(item,(str, tuple, list, set, dict)):
#             print(item, len(item))
#
# iterable_length(1, 34,"hello", 5+2j)


# x = 14
# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
# func(x)
# print('x is now', x)
#
# def func(a, b=5, c=10):
#     print('a is', a, 'and b is', b, 'and c is', c)
#
#
# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)

#
# def maximum(x, y):
#     if x > y:
#         return x
#     elif x == y:
#         return 'The numbers are equal'
#     else:
#         return y
#
#
# print(maximum(2, 3))

def fun(a=0):

    print(a)
fun(4)