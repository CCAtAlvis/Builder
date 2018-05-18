import os
import sys
import fnmatch
import subprocess

# TODO: proper variable naming
# TODO: maybe make this code modular

dirtobuild = "."
args = sys.argv
buildhome = False

# TODO: add proper agrs chacking
if len(args) > 1:
    if os.path.exists(args[1]):
        dirtobuild = args[1].replace('\\','/')
    else:
        print("the path you entered does not exist!")
        exit()

if len(args) > 2:
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
# TODO: proper building of .buildignore
for line in buildignorehandler:
    temp = ""
    for x in line:
        if x == "#" or x == "\n" or x == ' ':
            break
        else:
            temp += x

    if temp != "" or temp != " ":
        ignoreList.add('*'+temp+'*')

if '' in ignoreList:
    ignoreList.remove('')

f = list()
dirstoexplore = [dirtobuild,]
for (dirpath, dirnames, filenames) in os.walk(dirtobuild):
    f.append(dirpath)

for n in f:
    for ignore in ignoreList:
        if fnmatch.fnmatch(n[len(dirtobuild)+1:], ignore):
            break
    else:
        if n not in dirstoexplore:
            dirstoexplore.append(n)

for x in dirstoexplore:
    for (dirpath, dirnames, filenames) in os.walk(x):
        print(x.replace('\\', '/'))
        for files in filenames:
            print((x + os.sep + files).replace('\\', '/'))
            extn = x.split(".")[-1]

        break
    print()

