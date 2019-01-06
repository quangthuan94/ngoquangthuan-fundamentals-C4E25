p1 = {
    "name" : "Quan",
    "age": 22,
}

p2 = {
    "name": "Linh",
    "age": 25,
}

p3 = {
    "name": "Long",
    "age": 21,
}

p_list = []
print(p_list)

p_list.append(p2)
p_list.append(p3)
print(p_list)

for p in p_list:
    print(p("name"), p("age"))