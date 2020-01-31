import random

from EvictionPolicies.PoliciesAbstract import PoliciesAbstract


class RR(PoliciesAbstract):
    def __init__(self, capacity):
        self.index_map = {}
        self.entry_index = 0

    def find_evict_entry(self, cache):
        evict_entry_key = random.choice(list(self.index_map.keys()))
        self.index_map.pop(evict_entry_key)
        return evict_entry_key

    def process_while_entry(self, entry_key):
        if entry_key not in self.index_map:
            self.index_map[entry_key] = True
