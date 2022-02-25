# a = "hello world"
# l = a.split()
# d ={}
# for item in l:
#     if

"wap to create dictionary with first charachter and the word start with the charchter pair"
 # s = 'hello how are you all'
 # l =  s.split()
 # d =   defualtdict(tuple)
 #
 #
 # for item in l:
 #


# items = ["lotous-flowers", "lilly-flower", "cat-animal", "dog-animal", "sunflower-flower"]
# d = {}
#
# for item in items:
#     name, type_name = item.split("-")
#     if type_name not in d:
#         d[type_name] = [name]
#     else:
#         d[type_name] += [name]
# print(d)

"""print the number of occurence of charachters in a string without using inbuilt method"""\

# s = "hello world"
# d = {}
# for item in s:
#     if item not in d:
#         d[item] = 1
#     else:
#         d[item] += 1
# print(d)

"""writr a program to get index of each items in the below list"""
names = ["apple", "goole", "apple", "yahoo", "yahoo", "goole", "gmail", "gmail", "gmail"]
d = {}

for index,item in enumerate(names):
    if item not in d:
        d[item] = [index]
    else:
        d[item] = d[item] + [index]
print(d)
