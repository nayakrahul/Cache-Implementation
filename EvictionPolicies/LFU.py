from EvictionPolicies.PoliciesAbstract import PoliciesAbstract


class LFU(PoliciesAbstract):
    def __init__(self):
        self.freq_map = {}

    def find_evict_entry(self, cache):
        min_frequency = float("inf")
        evict_entry = None
        entry = cache.head
        while(entry is not None):
            if min_frequency > self.freq_map[entry.key]:
                min_frequency = self.freq_map[entry.key]
                evict_entry = entry
            entry = entry.next
        return evict_entry

    def process_while_entry(self, entry_key):
        if entry_key not in self.freq_map:
            self.freq_map[entry_key] = 1
        else:
            self.freq_map[entry_key] += 1

    def process_while_removal(self, entry_key):
        self.freq_map.pop(entry_key)
