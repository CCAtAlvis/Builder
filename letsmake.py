import re
import os
import sys

# print(sys.argv)
dirtobuild = "."

if len(sys.argv) > 1:
    dirtobuild = sys.argv[1]

ignoreList = set()

buildignore = open('.buildignore', 'r')

for line in buildignore:
    temp = ""
    for x in line:
        if x == "#" or x == "\n" or x == ' ':
            break
        else:
            temp += x

    if temp != "" or temp != " ":
        ignoreList.add(temp)

ignoreList.remove('')

# print(ignoreList) 

f = list()
for (dirpath, dirnames, filenames) in os.walk(dirtobuild):
    f.append(dirpath)

for string in f:
    for pattern in ignoreList:
        print(string, pattern, end="\t")
        print(re.search(pattern, string))
        if re.search(pattern, string) == None:
            # print(string)
            f.remove(string)

print("\n"*3)

for x in f:
    print(x)
