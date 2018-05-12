import re
import os
import sys

dirtobuild = "."
args = sys.argv
buildhome = False

if len(args) == 2:
    if os.path.exists(args[1]):
        dirtobuild = args[1]
    else:
        print("the path you entered does not exist!")
        exit()

if len(args) == 3:
    if os.path.exists(args[1]):
        dirtobuild = args[1]
    else:
        print("the path you entered does not exist!")
        exit()

    if args[2] == "--build-home":
        buildhome = True

settingpathignore = dirtobuild + os.sep + '.buildignore'
settingpathconfig = dirtobuild + os.sep + '.buildconfig'

buildignorehandler = ""
buildconfighandler = ""

if os.path.isfile(settingpathignore):
    buildignorehandler = open(settingpathignore, 'r')

if os.path.isfile(settingpathconfig):
    buildconfighandler = open(settingpathconfig, 'r')

ignoreList = set()
for line in buildignorehandler:
    temp = ""
    for x in line:
        if x == "#" or x == "\n" or x == ' ':
            break
        else:
            temp += x

    if temp != "" or temp != " ":
        ignoreList.add(temp)

if '' in ignoreList:
    ignoreList.remove('')

f = list()
dirstoexplore = list()
for (dirpath, dirnames, filenames) in os.walk(dirtobuild):
    f.append(dirpath)

for string in f:
    for pattern in ignoreList:
        if re.search(pattern, string) != None:
            break
    else:
        dirstoexplore.append(string)

if not buildhome:
    dirstoexplore.remove(dirtobuild)

filestobuild = list()
for x in dirstoexplore:
    # print(x)
    for (dirpath, dirnames, filenames) in os.walk(x):
        for files in filenames:
            filestobuild.append(x + os.sep + files)
            # print(x + os.sep + files, end = "\t")

        # print()
        break

for x in filestobuild:
    print(x)
