import re

# p = re.compile('a.[c]')
# u = re.compile('python')
# o = re.compile('ac[a-d]')
# i = re.compile('ab')
# m = p.match('a4c')
# m = p.match('zebra')
# n = u.search('aslkjsdjkdh python jksdfhvljkadhgl')

# print(n)
# print(m)

# result = p.findall("life is too short")
# print(result)


# p = re.compile("^python\s\w+", re.MULTILINE)
# data = """python one
# life is to short
# python two
# you need python
# python three"""
# print(p.findall(data))

# p = re.compile("\section")
# m = p.match("section")
# print(m)

# p = re.compile('short$')
# m = p.match("sexy girl")
# m = p.search("Life is too short")
# print(m)

p = re.compile(r'(\b\w+)\s+\1')
m = p.search('Paris in the the spring')
print(m.group())
