from EvictionPolicies import Heap
from EvictionPolicies import PoliciesAbstract


class LFU(PoliciesAbstract):
    def __init__(self, capacity):
        self.freq_map = {}
        self.heap = Heap(capacity, self.freq_map)

    def find_evict_entry(self, cache):
        evict_entry_key = self.heap.extract_min()
        self.freq_map.pop(evict_entry_key)
        return evict_entry_key

    def process_while_entry(self, entry_key):
        if entry_key not in self.freq_map:
            self.freq_map[entry_key] = 1
            self.heap.insert(entry_key)
        else:
            temp = self.freq_map[entry_key] + 1
            self.heap.delete(entry_key)
            self.freq_map[entry_key] = temp
            self.heap.insert(entry_key)
