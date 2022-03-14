import pyautogui as pg
import time
time.sleep(10)

for i in range(100):
    pg.write('I LOVE YOU VISHAL LODA PIYU LODU')
    pg.press('enter')


#
# a = "1"
# t = (1)
#
# from sys import getsizeof
# print(getsizeof(a))
#
# print(getsizeof(t))


# def even():
#     for item in range(1, 51):
#         if item % 2 == 0:
#             yield item
# # even_num = even()
# # print(even_num)
# # print(list(even_num))
#
#
# even = (item for item in range(1,51) if item %2 == 0)
# print(list(even))
"""Write a generator function to yield the names  starting with vowel  in the given list"""

# names = ["john", "eve", "bob", "emma", "ana"]
#
#
# def vowels(iterable):
#     for item in iterable:
#         if item[0].lower() in "aeiou":
#             yield item
#
#
# v = vowels(names)
# print(list(v))
#
# vowel = (item for item in names if item[0].lower() in 'aeiou')
# print(list(vowel))

"""write a generator function and expression to yield length of each line in file only if the line is not empty"""

path = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\txt_log_files\sample.txt"

# def length_of_lines(input_):
#     with open(input_) as file:
#         for line in file:
#             if line.strip():
#                 yield len(line)
#
# print(list(length_of_lines(path)))
#
# with open(path) as file:
#     out = (len(line)for line in file if line.strip())
#     print(list(out))

a = "hello welcome to the python"
s = a.split()
s1 = ','.join(s)
print(s1)