# f_path = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\txt_log_files\sample.txt"
# path = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\txt_log_files\sample.txt"
#
# with open(path, "r") as file_read, open(f_path, "w") as file_write:
#     for line in file_read:
#         file_write.write(line)
#
import csv

# with open("example.csv", "w") as csv_:
#     write_obj = csv.writer(csv_)
#     write_obj.writerow(["x", "y", "z"])
#     write_obj.writerows([(1, 2, 3), (5, 6, 7), (8, 9, 10)])

e_path = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\csv_files\employees.csv"

# with open (e_path) as csv_obj:
#     obj = csv.reader(csv_obj)
#     for raw in obj:
#         print(raw[0])


"""Wap to print only the salaries that are >70000"""

# with open(e_path) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     for raw in r_obj:
#         if int(raw[3]) > 70000:
#             print(raw[0])

"""Wap to group male and female employee in the file"""

# with open(e_path) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     d = {"male": [], "female": []}
#     for row in r_obj:
#         if row[1] == "male":
#             d["male"] += [row[0]]
#         else:
#             d["female"] += [row[0]]
#     print(d)

# from collections import defaultdict
# with open(e_path) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     dd = defaultdict(list)
#
#     for row in r_obj:
#         dd[row[1]] += [row[0]]
#     print(dd)
#

"""Wap to group employees based on their item"""

# from collections import defaultdict
# with open(e_path) as file:
#     r_obj = csv.reader(file)
#     header = next(r_obj)
#     dd = defaultdict(list)
#
#     for row in r_obj:
#         dd[row[2]] += [row[0]]
#     print(dd)

"""Wap to sort the shares in test.csv file based on the share price"""
# path1 = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\csv_files\test.csv"
#
# with open(path1) as file:
#     r_obj = csv.DictReader(file)
#     l = list(r_obj)
#     res = sorted(l, key=lambda d: float(d["price"]))
#     print(list(res))
#

"""Wap to add all the shares in test.csv file"""
# p = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\csv_files\test.csv"
# with open(p) as file:
#     r_obj = csv.reader(file)
#     res = 0
#     next(r_obj)
#     for row in r_obj:
#         res += float(row[2])
#     print(res)


"""get the latest updaeted country with its total vaccination and number of people vaccination"""

# path = r"C:\Users\sanji\PycharmProjects\pythonProject1\files_directory\csv_files\vaccination_data.csv"
# from collections import defaultdict
# with open(path)as file:
#     r_obj = csv.DictReader(file)
#     header = next(r_obj)
#     d = defaultdict(list)
#     for row in r_obj:
#         d[row["DATE_UPDATED"]]  += [(row["COUNTRY"], row["TOTAL_VACCINATIONS"])]
#
#
# res = sorted(d.items())
# print(res[-1])
# for item in res:
#     print(item)
