from xml.etree.ElementTree import Element, SubElement, dump, ElementTree, parse

def indent(elem, level=0):
    i= "\n" + level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem :
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

blog = Element("blog")
blog.attrib["date"] = "20180108"
blog.attrib["editor"] = "pycharm"

subject = Element("subject")
subject.text = "Why python?"
blog.append(subject)

author = Element("author")
author.text = "Eric"
blog.append(author)

SubElement(author, "age").text = "58"
SubElement(author, "nation").text = "USA"

Agenda = Element("Agenda")
blog.append(Agenda)
SubElement(Agenda, "a").text = "Data Type"
SubElement(Agenda, "b").text = "Controll Flow"
SubElement(Agenda, "c").text = "Function"

print("blog")
indent(blog)
dump(blog)

print("subject")
subject_tag = blog.find("subject")
print(subject_tag.text)

print("author의 자식 노드")
author_tags = blog.findall("author")
for i in author_tags:
    for j in i :
        print(j.text)
print("Agenda의 자식 노드")
childs = blog.getiterator("Agenda")
for i in childs:
    for j in i :
        print(j.text)

print("blog xml 생성")
ElementTree(blog).write("blog.xml")

tree = parse("blog.xml")
blog = tree.getroot()

print("keys값 ,속성")
print(blog.keys())
print(blog.items())

