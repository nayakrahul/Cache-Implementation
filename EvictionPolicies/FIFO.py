from datetime import datetime

from EvictionPolicies.Heap import Heap
from EvictionPolicies.PoliciesAbstract import PoliciesAbstract


class FIFO(PoliciesAbstract):
    def __init__(self, capacity):
        self.created_on_map = {}
        self.heap = Heap(capacity, self.created_on_map)

    def find_evict_entry(self, cache):
        evict_entry_key = self.heap.extract_min()
        self.created_on_map.pop(evict_entry_key)
        return evict_entry_key

    def process_while_entry(self, entry_key):
        if entry_key not in self.created_on_map:
            self.created_on_map[entry_key] = datetime.now()
            self.heap.insert(entry_key)
