from Exceptions import HeapOverflow


class Heap:
    def __init__(self, capacity, comparison_map):
        self.heap = []
        self.capacity = capacity
        self.comparison_map = comparison_map

    def _compare(self, i, j):
        return self.comparison_map[self.heap[i]] > self.comparison_map[self.heap[j]]

    def _swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def _parent(self, i):
        return int((i-1)/2)

    def _left(self, i):
        return 2*i + 1

    def _right(self, i):
        return 2*i + 2

    def insert(self, key):
        if len(self.heap) > self.capacity:
            raise HeapOverflow()
        self.heap.append(key)
        i = len(self.heap) - 1
        while i != 0 and self._compare(self._parent(i), i):
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def update_key(self, i, new_val):
        self.comparison_map[self.heap[i]] = new_val
        while i != 0 and self._compare(self._parent(i), i):
            self._swap(i, self._parent(i))
            i = self._parent(i)

    def extract_min(self):
        root = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self.heapify(0)
        return root

    def delete(self, key):
        self.update_key(self.heap.index(key), float("-inf"))
        self.extract_min()

    def heapify(self, i):
        l = self._left(i)
        r = self._right(i)
        smallest = i
        if l < len(self.heap) and self._compare(i, l):
            smallest = l
        if r < len(self.heap) and self._compare(smallest, r):
            smallest = r
        if smallest != i:
            self._swap(i, smallest)
            self.heapify(smallest)
