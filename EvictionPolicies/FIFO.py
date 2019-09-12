from datetime import datetime

from EvictionPolicies.PoliciesAbstract import PoliciesAbstract


class FIFO(PoliciesAbstract):
    def __init__(self):
        self.created_on_map = {}

    def find_evict_entry(self, cache):
        min_created_on = datetime.max
        evict_entry = None
        entry = cache.head
        while(entry is not None):
            if min_created_on > self.created_on_map[entry]:
                min_created_on = self.created_on_map[entry]
                evict_entry = entry
            entry = entry.next
        return evict_entry

    def process_while_entry(self, entry):
        if entry not in self.created_on_map:
            self.created_on_map[entry] = datetime.now()
