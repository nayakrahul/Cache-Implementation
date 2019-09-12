from Cache import Cache
from EvictionPolicies.LFU import LFU
from EvictionPolicies.LRU import LRU
from EvictionPolicies.FIFO import FIFO


cache = Cache(LFU())
cache.add(2,4)
cache.add(1,3)
cache.add(10,30)
cache.add(2, 5)
cache.add(10, 6)
cache.add(8,9)
print(cache.display())
print(cache.get_value(5))
