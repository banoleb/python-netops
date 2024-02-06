#!/usr/bin/env python3


#TASK6.1
mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []
for i in mac:
    result.append(i.replace(':', '.'))
print(result)