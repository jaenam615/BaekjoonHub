from collections import deque

class DoubleSidedQueue():
    size: int
    pop_list: list
    arr: deque

    def __init__(self, size: int, pop_list: list):
        self.size = size
        self.pop_list = pop_list
        self.arr = deque(i for i in range(1, size + 1))  

    def shift_left(self):
        temp_arr = list(self.arr)
        first = temp_arr[0]

        for i in range(len(temp_arr) - 1):
            temp_arr[i] = temp_arr[i + 1]

        temp_arr[-1] = first
        self.arr = deque(temp_arr)
     
    def shift_right(self):
        temp_arr = list(self.arr)
        last = temp_arr[-1]

        for i in range(len(temp_arr) - 1, 0, -1):
            temp_arr[i] = temp_arr[i - 1]

        temp_arr[0] = last
        self.arr = deque(temp_arr)

    def solution(self):
        count = 0

        for target in self.pop_list:
            idx = self.arr.index(target)

            if idx <= len(self.arr) // 2:
                for _ in range(idx):
                    self.shift_left()
                    count += 1
            else:
                for _ in range(len(self.arr) - idx):
                    self.shift_right()
                    count += 1

            self.arr.popleft() 
        return count

if __name__ == "__main__":
    N, M = map(int, input().split())
    pop_list = list(map(int, input().split()))

    dsq = DoubleSidedQueue(N, pop_list)
    print(dsq.solution())
