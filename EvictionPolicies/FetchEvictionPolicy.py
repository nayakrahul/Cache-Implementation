from EvictionPolicies import RR
from EvictionPolicies import LFU
from EvictionPolicies import LRU
from EvictionPolicies import FIFO
from Exceptions import EvictionPolicyNotFound


def fetch_eviction_policy(arg, capacity):
    arg = arg.lower()
    if arg == 'lru':
        return LRU()
    elif arg == 'lfu':
        return LFU(capacity)
    elif arg == 'fifo':
        return FIFO(capacity)
    elif arg == 'rr':
        return RR(capacity)
    else:
        raise EvictionPolicyNotFound()
