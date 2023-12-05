# assumes file name main.lean
# assumes theorem `theorem test : 1 + 1 = 2 :=`
flag = False
with open('main.lean') as mainlean:
  for ln in mainlean:
    if ln.startswith("theorem test : 1 + 1 = 2 :="):
      print("theorem statement exists")
      flag = True
      break
if flag is False:
  print(1/0)
