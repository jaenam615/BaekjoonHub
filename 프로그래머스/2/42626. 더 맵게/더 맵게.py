import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while True:
        if scoville[0] >= K:
            return answer
                
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville) * 2

        val = first + second
        answer += 1
        
        heapq.heappush(scoville, val)
