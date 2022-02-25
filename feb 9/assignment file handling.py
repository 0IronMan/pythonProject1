path = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\txt_log_files\sample.txt"

""" 15. Finding the length of each line in the text file"""

# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 0
#         l = line.split()
#         print((f'line no {count}', f'total no of words{len(l)}'))
#
# with open(path) as file:
#     for line in file:
#         print(line, len(line), end=" ")
#
#
# """	16. Extracting message form sample.log"""
path1 = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\txt_log_files\sample.log"

with open(path1) as file:
    count = 0
    for line in file:
        l = line.split()
        for l[2] in l:
            print(l[2], l.count(l[2]))

"""Reading countries from fotball.txt"""

# path = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\txt_log_files\football.txt"
#
# with open(path, encoding="UTF-8") as file:
#     for line in file:
#         if line.strip():
#             country = line.split("\t")
#             print(country)

"""Least and most occurances of the word"""

\


# with open(path) as file:
#     for line in file