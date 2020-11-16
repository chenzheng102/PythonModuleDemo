from collections import namedtuple

point = namedtuple("point",["x","y","b"])
b = point(1,2,5)
print(b.x)
print(b.b)
from collections import deque
duqued = deque([1,2,4,5])
duqued.append("kjlj")
duqued.appendleft("left")
print(duqued)

f = [x*y for x in range(10) if x >5 for y in range(10000000)]
print(f)