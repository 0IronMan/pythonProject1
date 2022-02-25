# a = ["acd", "b"]
#
#
# def func(char):
#     print([char])
#
#
# res = map(func, a)
# list(res)
#
#
#
#
# res1 = list(map(list, a))
# print(res1)



# l = ["hai", "hello", 2, 2.5, 3+5j, True]
# dd = {index: element[::-1] if isinstance(element, str) else element for index, element in enumerate(l)}
# print(dd)


# l = [10, 20, 30, 40]

# Method 1: by using lambda function

# square = lambda num: num**2
#
# print(list(map(square, l)))


l = [10, 20, 30, 40, 40]


def square(item):
    if item[0] % 2 == 0:
        res = item[1] ** 2
        return res


output = list(filter(square, enumerate(l)))
print(list(map(square, output)))
