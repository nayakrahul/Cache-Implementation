import sys
from Cache import Cache

if len(sys.argv) < 2:
    print("Error: Pass eviction policy as argument")
    sys.exit()

cache = Cache(sys.argv[1])
cache.add(2,4)
cache.add(1,3)
cache.add(10,30)
cache.add(2, 5)
cache.add(1, 6)
cache.add(8,9)
cache.display()
