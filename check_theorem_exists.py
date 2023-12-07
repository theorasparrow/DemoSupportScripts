import os

# get commented open theorem from main branch
# raw files in main branch
root = "https://raw.githubusercontent.com/theorasparrow/LeanDemo/main/"
currentmainpath = 'src/main.lean'
currentoldfile = root + currentpath

with open(currentoldfile) as currentoldlean:
  for ln in currentoldlean:
    if ln.startswith("-- theorem"):
      print("commented open theorem from main branch: ", ln[2:])

# assumes file name main.lean
# assumes theorem `theorem test : 1 + 1 = 2 :=`
flag = False
with open('src/main.lean') as mainlean:
  for ln in mainlean:
    if ln.startswith("theorem test : 1 + 1 = 2 :="):
      print("theorem statement exists")
      flag = True
      break
if flag is False:
  print(1/0)





# for path, subdir, files in os.walk('src'):
#   for name in files:
#     # paths of files
#     currentpath = os.path.join(path, name)
#     print(currentpath)
#     with open(currentpath) as currentlean:
#       for ln in currentlean:
#         if ln.startswith("theorem test2 : 2 + 2 = 4 :="):
#           print("open theorem exists")
#           flag = True
#           break
#     if flag is False:
#       print(1/0)
