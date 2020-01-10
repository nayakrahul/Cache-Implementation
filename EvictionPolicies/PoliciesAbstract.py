from abc import ABC, abstractmethod


class PoliciesAbstract(ABC):
    @abstractmethod
    def find_evict_entry(self, cache):
        pass

    @abstractmethod
    def process_while_entry(self, entry_key):
        pass

    @abstractmethod
    def process_while_removal(self, entry_key):
        pass
