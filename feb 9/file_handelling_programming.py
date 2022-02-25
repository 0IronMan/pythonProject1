from collections import defaultdict, Counter
#path = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\txt_log_files\sample.txt"
# path = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\txt_log_files\access-log.txt"
"""Wap to read all the line in a file without loading the file in the memory"""
#
# with open(path) as file:
#     for line in file:
#         # print(line)

"""Wap to count the number of line present in the file"""

# with open (path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     print(count)
#
# """Wap to print line number and line from the file"""
#
# with open (path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         print(count, line)
#
# """Wap to count the number of words in the given files"""
#
# with open (path) as file:
#     count = 0
#     for line in file:
#         words = line.split()
#         for word in words:
#             count += 1
#     print(count)
#
# """Wap to print the lines from the last of the file """
#
# with open (path) as file:
#     for line in reversed(list(file)):
#         print(line)
#
# """Wap to count the number of spaces in the given files"""
#
#
 # or
#
#
# with open (path) as file:
#     count = 0
#     for line in file:
#         spaces = line.count(" ")
#         count += spaces
#     print(count)

"""Wap to count the number of word is starting with vowels"""

with open (path) as file:
    count = 0
    for line in file:
        for word in line.split():
            if word[0] in "aeiouAEIOU":
                count += 1
    # print(count)

"""WAP TO create a dictionary of word its count pair in the given file"""

with open (path) as file:
    d = {}
    for line in file:
        for word in set(line.split()):
            if word not in d:
                d[word] = line.split().count(word)
            else:
                d[word] += line.split().count(word)
    # print(d)

"""Wap to extract all the Ip address from access log.txt file"""


# with open (path) as file:
#     l = []
#     for line in file:
#         if line.strip():
#             word = line.split()
#             l.append(word[0])
#     # print(l)
# ip_ = Counter(l)
# print(ip_)
# print(ip_.most_common(1))
"""Wap to create  dictionary of ip address and they count"""

path1 = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\txt_log_file s\access-log.txt"

# with open (path1) as file:
#     l = []
#     for line in file:
#         if line.strip():
#             list_ = line.split()
#             l.append(list_[0])
#
# 
# d = {item: l.count(item) for item in l}
# print(d)
#
# ip_ = Counter(l)
# print(ip_)

"""Wap to print nth line in a file"""
# path = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\txt_log_files\access-log.txt"
# with open (path1) as file:
#     n = 3
#     for line in enumerate(file, start=1):
#         if line == n:
            # print(line)

"""Wap to print first N lines"""
path2 = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\txt_log_files\access-log.txt"

# with open (path2) as file:
#     n = 3
#     for line in range(n+1):
#         # print(line)

"""Wap to print last n line"""

path = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\txt_log_files\sample.txt"
n = 5
with open (path) as file:
    count = 0
    for line in file:
        count += 1
    file.seek(0)
    res = islice(file, count-n, count)
    print (res)