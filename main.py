global code
global final
from pathlib import Path
import os
import glob

decount = 0
count = 0
ifcount = 0
cocount = 0
ccount = {}
try:
  with open("pine.pine", "+r") as myfile:
    code = myfile.read()
    print()
except Exception as e:
  code = "1 2 3"
  a = os.path.dirname(os.path.realpath(__file__))
  path1 = Path(a)
  path3 = glob.glob(a)
  path2 = os.listdir(path3[0])
  for files in path2:
    if ".pine" in files:
      final = files
      break
    decount += 1
  if a[0] == '\\':
    with open(a + "\\" + path2[decount], "+r") as myfile:
      code = myfile.read()
  else:
    with open(a + "/" + path2[decount], "+r") as myfile:
      code = myfile.read()
vv = code.split()
for i in vv:
  ifcount = 0
  cocount = 0
  if "=" in vv[count]:
    for i in vv[count]:
      if vv[count][cocount] == "=":
        ccount[vv[count][:cocount]] = vv[count][cocount + 1:]
      cocount += 1
  if "print" in vv[count]:
    try:
      if ccount[vv[count][6:]] == None:
        print("?")
      print(ccount[vv[count][6:]])
    except:
      print(vv[count][6:])

  count += 1
