
decount = 0
count = 0
ifcount = 0
compile = "pine.pine"
#컴파일 할 코드 
cocount = 0
ccount = {}
with open(compile, "+r") as myfile:
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
