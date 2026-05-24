list = [0,0,0,1,1,1]
tipos = sorted(set(list))

print(list)
print(tipos)
type_index = []

for tipo in tipos:
    nodesOfType = [i for i, t in enumerate(list) if t == tipo]
    type_index.append(nodesOfType)

print(type_index)