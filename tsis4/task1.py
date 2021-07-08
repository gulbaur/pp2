import re
file=open('data.txt',encoding="utf8")
text = file.read()
BIN = re.search(r"БИН.*(?P<BIN>\b[0-9]+)", text).group("BIN")
Name = re.search(r"Филиал.*(?P<Name>\b[A-Z]+)", text).group("Name")
print(BIN )
print(Name)


item = re.compile(r"(?P<title>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total>.*)")


for m in re.finditer(item, text):
    print(m.group("title") + "\n"  + m.group("count")+ "\n" + m.group("price") + "\n"+ m.group("total"))

Time = re.search(r"\nВремя: (?P<Time>\b[0-9].*\n{1}(?P<Address>.*))", text).group("Time")
Address = re.search(r"\nВремя: (?P<Time>\b[0-9].*\n{1}(?P<Address>.*))", text).group("Address")
print(Time)