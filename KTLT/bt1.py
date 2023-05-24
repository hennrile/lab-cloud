# with open("test.txt", "a+", encoding="utf-8") as f:
#     f.seek(0)
#     data = f.readlines()

# print(data)

# a = []
# for i in data:
#     a.append(i.strip().split())

# # print(a)
# lst = []

# for i in a:
#     for x in i:
#         lst.append(x.strip().split()) 

# # print(lst)
# newlst = []

# for x in lst:
#     print(x)
#     if x.isdigit() == True:
#         newlst.append(x)

import re

with open('test.txt', 'r', encoding="utf-8") as f:
    data = f.read()

result = re.findall(r'\d+', data)

print(result)