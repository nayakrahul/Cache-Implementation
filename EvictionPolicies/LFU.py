from EvictionPolicies.PoliciesAbstract import PoliciesAbstract


class LFU(PoliciesAbstract):
    def __init__(self):
        self.freq_map = {}

    def find_evict_entry(self, cache):
        min_frequency = float("inf")
        evict_entry = None
        entry = cache.head
        while(entry is not None):
            if min_frequency > self.freq_map[entry]:
                min_frequency = self.freq_map[entry]
                evict_entry = entry
            entry = entry.next
        return evict_entry

    def process_while_entry(self, entry):
        if entry not in self.freq_map:
            self.freq_map[entry] = 1
        else:
            self.freq_map[entry] += 1
