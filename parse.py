"""
将日志排序
"""

import re

f = open("item.txt", "r")
items = f.readlines()
f.close()

print(len(items))
_items = []
for item in items:
    item = re.sub('\n', '', item)
    it = item.split(' ')
    it = [int(it[1]), int(it[0])]
    if it not in _items:
        _items.append(it)

_items.sort(reverse=True)
for i in _items:
    ff = open("new.item.txt", "a")
    ff.write(str(i[1]) + ' ' + str(i[0]) + '\n')
    ff.close()