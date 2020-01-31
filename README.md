# Cache-Implementation
Implemented cache with plugable eviction policies like FIFO, LRU, LFU, RR.

Each eviction policy has:
* logic to find key to be evicted
* method to maintain a eviction logic system

### How to use cache
It is provided in `testit.py`
