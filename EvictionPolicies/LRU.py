from EvictionPolicies import PoliciesAbstract


class LRU(PoliciesAbstract):
    def find_evict_entry(self, cache):
        return cache.tail.key

    def process_while_entry(self, entry_key):
        pass
