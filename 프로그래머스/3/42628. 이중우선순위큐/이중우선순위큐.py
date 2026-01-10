import heapq

class DoubleHeap:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.count = {}
    
    def decide(self, k, v):
        if k == 'I':
            self._insert(v)
        else:
            if v == 1:
                self._delete_max()
            elif v == -1:
                self._delete_min()
    
    def _insert(self,v):
        heapq.heappush(self.min_heap, v)
        heapq.heappush(self.max_heap, -v)
        self.count[v] = self.count.get(v, 0) + 1
    
    def _delete_min(self):
        while self.min_heap:
            x = heapq.heappop(self.min_heap)
            if self.count.get(x, 0) > 0:
                self.count[x] -= 1
                break

    def _delete_max(self):
        while self.max_heap:
            x = -(heapq.heappop(self.max_heap))
            if self.count.get(x, 0) > 0:
                self.count[x] -= 1
                break
                
    def get_min(self):
        while self.min_heap:
            x = heapq.heappop(self.min_heap)
            if self.count.get(x, 0) > 0:
                return x
        return 0

    def get_max(self):
        while self.max_heap:
            x = -heapq.heappop(self.max_heap)
            if self.count.get(x, 0) > 0:
                return x
        return 0

def solution(operations):
    dheap = DoubleHeap()
    for operation in operations:
        k = operation.split(' ')[0]
        v = int(operation.split(' ')[1])
        dheap.decide(k, v)

    answer = [dheap.get_max(), dheap.get_min()]
    return answer