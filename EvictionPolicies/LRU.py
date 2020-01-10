from EvictionPolicies.PoliciesAbstract import PoliciesAbstract


class LRU(PoliciesAbstract):
    def find_evict_entry(self, cache):
        return cache.tail

    def process_while_entry(self, entry_key):
        pass

    def process_while_removal(self, entry_key):
        pass
