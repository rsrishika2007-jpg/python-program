d={"eno":123,"ename":"Abc"}
print(d)
print(d["eno"])
print(d.get("ename"))
d["ename"]="ris"
print(d)
d["age"]=9
print(d)
for value in d.values():
  print(value)
for key in d:
  print(key)
for key,value in d.items():
  print(key,":",value)
d.pop("eno")
print(d)
d.popitem()
print(d)
