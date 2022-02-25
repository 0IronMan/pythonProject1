""""wap to print "banglore"10 times without using for loop"""
# a = "banglore"
# print(a*10)

""" wap to count the number of digit and alphabets in the string"""
# a = "hai 1234 python234"
# digit = letter = 0
#
#
# for i in a:
#     if i.isdigit():
#         letter = letter+1
#     elif i.isalpha():
#         digit = digit + 1
#     else:
#         pass
# print("digits:", digit)
# print("letters:",letter)

"""""wap to create string by swaping the case of the charachters without using in built method"""""
# a = input()
# new =""
#
#
# for i in range(len(a)):
#     if 'a' <= a[i] <= 'z':
#         new = new + chr(ord(a[i])- 32)
#     elif 'A' <=a[i] <= 'Z':
#         new = new + chr(ord(a[i])+32)
#
# print (new)
"""wap to create string with only constanant present in the string """
# a = "python selenium"
#
# res = ""
#
# for chr in a:
#     if chr.lower()
"""wap to serch for a charactor in the string and return its first occurance postion"""
# s = "simple"
# chr = ""
# for item in s:
#     if chr == item:
#         ind = s.index(chr)
#         print (f"{chr}is present at index {ind}")
#         break
"""wap to print th character and its ascii value if the charater is wovel in the string """
a = "she sells sea shells on the sea share"
#
# for ele in a:
#     if ele.lower() in "aoieu":
#         print(ord(ele))


""" traversing a string in reversed order """
# string = "hai"

# for item in range(len(string)-1, -1, -1):
#     print(string[item], end=" ")
#
# print()
#
# for char in string[::-1]:
#     print(char, end=" ")
#
# print()
# for item in reversed(string):
#     print(item, end=" ")

""" count the number of characters in a string """
# string = "hello world"

# count = 0
# for _ in string:
#     count += 1
# """wap to print word and its length"""
# s = "hello world"
# words = s.split()
# for i in words:
#     print(i,len(i))


l = [1, 6, -3, 9, -3, -4, 1, -1]

def convert_(num):
    return abs(num)

con = lambda num: abs(num)

res = map(abs, l)
print(list(res))

