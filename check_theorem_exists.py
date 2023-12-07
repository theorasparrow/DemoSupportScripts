import os
from urllib import request

# get commented open theorem from main branch
# raw files in main branch
root = 'https://raw.githubusercontent.com/theorasparrow/LeanDemo/main/'
currentmainpath = 'src/main.lean'
currentoldfile = root + currentmainpath
currentopentheorem = ''
with request.urlopen(currentoldfile) as f:
  for ln in f.read().decode().splitlines():
    if ln.startswith('-- theorem'):
      currentopentheorem = ln.split(':=')[0][3:]
      print("current open theorem:", currentopentheorem)


flag = False
with open(currentmainpath) as mainlean:
  for ln in mainlean:
    if ln.startswith(currentopentheorem):
      print("theorem statement exists")
      flag = True
      break
if flag is False:
  print(1/0)


for path, subdir, files in os.walk('src'):
  print('paths in repo')
  for name in files:
    currentpath = os.path.join(path, name)
    print(currentpath)
