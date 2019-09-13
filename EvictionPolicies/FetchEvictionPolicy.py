from EvictionPolicies.LFU import LFU
from EvictionPolicies.LRU import LRU
from EvictionPolicies.FIFO import FIFO
from Exceptions import EvictionPolicyNotFound


def fetch_eviction_policy(arg):
    arg = arg.lower()
    if arg == 'lru':
        return LRU()
    elif arg == 'lfu':
        return LFU()
    elif arg == 'fifo':
        return FIFO()
    else:
        raise EvictionPolicyNotFound()
