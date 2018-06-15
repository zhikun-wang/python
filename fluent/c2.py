colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(c, s) for c in colors for s in sizes]
print(tshirts)

import os

path, file_name = os.path.split("/Users/tim/Workspace/python/fluent/2.4.py")
print(path, '====', file_name)

li = [1, 2, 3]
print(id(li))
li *= 2
print(id(li))
li = li * 2
print(id(li))

t = (1, 2, [30, 40])
try:
    print(t)
    t[2] += [50, 60]
except TypeError as e:
    print("Error", e)

print(t)
