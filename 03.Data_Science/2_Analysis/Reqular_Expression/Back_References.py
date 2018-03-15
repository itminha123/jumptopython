import re

# p = re.compile(r"(\w+)\s")
# p = re.compile(r"(\w+)\s(\w+)")
# p = re.compile(r"(\w+)\s\1")
# m = p.search("sdf Hello Hello")
# print(m)
#
# p = re.compile(r"(\w+)\s(\w+)\s\1\s\2")
# m = p.search("sdf Hello World Hello World")
# print(m)

# p = re.compile(r"(?P<greeting>\w+)\s\1")
# m = p.search("sdf Hello Hello")
# print(m.group("greeting"))

# p = re.compile(r"(?P<greeting>\w+)\s(?P<destination>\w+)\s\1\s\2")
# m = p.search("sdf Hello World Hello World")
#
# print(m)
# print(m.group("greeting"))
# print(m.group("destination"))

p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())