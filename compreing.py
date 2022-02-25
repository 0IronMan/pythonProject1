#wap to create a list at tuples which is having index and its corrosponding items
#l=["pytho",10,34,5.3,"selinuun","java" ]
# l_index=[]
#
# for item in enumereate(l):
# #     l_index.apeend(item)
# # print(l_index)
# l_index= [(index,item) for index, item in enumerate(l)]
# print(l_index)
#l = [1,2,3,4,5,6,7,8]
#even=[item for item in l if item% 2 == 0]
#print(even)
#compression
# l=list(range(10))
# even=[i for i in l if i % 2 == 0]
# odd = [i for i in l if i % 2 != 0]

""" wap to create a listusing the following list if the word is even store as it if odd to store reverse string"""

# l=["python","node Js","selenium","simple"]
# res=[item if len(item)%2 == 0 else item [::-1] for item in l]
# print(res)
# """reverse if it is a string else keep it as it is"""
# list_ = ["java", "python", "c++", "rubby", "amazon"]
# output = []
#
# for item in list_:
#     if isinstance(item, str):
#         output.append(item[::-1])
#     else:
#         output.append(item)
# print(output)
# #compression
# output = [str(item)[::-1] if not isinstance(item, str) else item for item in list_]
# print(output)


#write a list compression to create a list with the string starting with vowels

# vowels = [item for item in list_ if item[0].lower() in "aeiou"]
# print(vowels)
"""wap to create a set of squre from 1 to 10"""
# res = set()
# for i in range(1,11):
#     res.add(i**2)
# print(res)
# res = {i ** 2 for i in range(1, 11)}
#print(res)

""" write a set compression to create set of tupple of item and index"""
# l = ["java", "python", 10, True, 1.4, "c++", "rubby"]
# res = {(index, item) for index, item in enumerate(l)}
# print(res)

"""write a set compressi0on to creat set of tupple with item and length pair"""
# files = ("amozone", "flipcart", "walmart", "gmail", "yahoo")
# set_ = {(item, len(item)) for item in files}
# print(set_)