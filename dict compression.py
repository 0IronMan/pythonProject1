# """wap to create dictionary with item and its index pair"""
# string = "hello"
# d = {}
#
#  for index, item in enumerate(string):
#      d[item] = index
#  print(d)
"""wap to create a dictionary with world and its lengthy pair"""
# a = "hello world welcome  to pytho "
# words = a.split()
# d ={}
#
# for word in words:
#     d[word] = len[word]
# print(d)
"""wap to with char and compare """
#a = "hello"
# d = {}
# for chr in a:
#     d[chr] = a.count(chr)
# print(d)
#
# d_ = {chr: a.count(chr) for chr in a}
# print(d_)

"""wap to create dictionary of word and its count"""
#sentence = "python is language, python programing is easy"
# words = sentence.split()
# d = {}
#  for word in words:
#      d[word] = words.count(word)
# print(d)



"""dictionary with word and its length pair only if the word is of even length"""

#sentence = "python is language, python programing is easy"
#dd = {word: words.count(word)for word in word if len(word) % 2== 0}
#print(dd)

"""dictionary with index and word pair if the word is of odd lenth   else keep it as is"""
#sentence = "python is language, python programing is easy"
# words = sentence.split()
# d = {}
#
# for index, word in enumerate  (words):
#     if len (word) % 2 == 0:
#         d[index] = word
#     else:
#         d[index] = word[::-1]
# l = ['sanjit', 'python','orange',12, 3.5,'cool']
# d = {index: item[::-1] if isinstance(item, str) else item for index, item in enumerate(l)}
# print(d)


