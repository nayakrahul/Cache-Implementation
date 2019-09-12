from Entry import Entry
from Exceptions import CacheMiss

CACHE_SIZE = 3


class Cache:
    def __init__(self, eviction_policy):
        self.head = None
        self.tail = None
        self.map = {}
        self.size = CACHE_SIZE
        self.eviction_policy = eviction_policy
        self.total_tries = 0
        self.cache_hits = 0

    def create_entry(self, key, value):
        entry = Entry(key, value)
        return entry

    def add(self, key, value):
        if key in self.map:
            entry = self.map[key]
            self.remove_entry(entry)
            entry.value = value
            self.head, self.tail = self.add_entry(self.head,
                                                  self.tail,
                                                  entry)

        else:
            entry = self.create_entry(key, value)
            if len(self.map) < self.size:
                self.head, self.tail = self.add_entry(self.head,
                                                      self.tail,
                                                      entry)
            else:
                temp = self.tail.previous
                evict_entry = self.eviction_policy.find_evict_entry(self)
                # print(evict_entry)
                self.remove_entry(evict_entry)
                self.tail = temp
                self.head, self.tail = self.add_entry(self.head,
                                                      self.tail,
                                                      entry)
        self.map[key] = entry

    def add_entry(self, head, tail, entry):
        if head is None and tail is None:
            entry.previous = None
            entry.next = None
            tail = entry
        else:
            entry.next = head
            head.previous = entry
            entry.previous = None
        self.eviction_policy.process_while_entry(entry)
        return entry, tail

    def remove_entry(self, entry):
        prev_entry = entry.previous
        next_entry = entry.next
        prev_entry.next = next_entry
        if next_entry is not None:
            next_entry.previous = prev_entry

    def get_value(self, key):
        self.total_tries += 1
        try:
            entry = self.map[key]
            self.cache_hits += 1
            return entry.value
        except KeyError:
            raise CacheMiss("key not found in cache")

    def display(self):
        entry = self.head
        while(entry is not None):
            print(entry.key, entry.value)
            entry = entry.next

    def calculate_hit_ratio():
        return cache_hits/total_tries
