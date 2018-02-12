
"""
将图片排序
"""
import os, os.path, shutil, re

images = os.listdir(r"路径")

f = open("new.item.txt", "r")
items = f.readlines()

_items = []
for i in range(len(items)):
    item = items[i]
    item = re.sub(r'\n', '', item)
    it = item.split(' ')
    it.append(str(i))
    _items.append(it)


for img in images:
    pid = re.search(r'^(\d+?)_\S+?', img).group(1)
    for item in _items:
        if item[0] == pid:
            shutil.copy("hequanshawu/" + img, "index/" + item[2] + "_" + img)
            print(pid + "复制成功")