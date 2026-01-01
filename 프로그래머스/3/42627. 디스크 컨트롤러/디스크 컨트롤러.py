import heapq

def solution(jobs):
    time = 0
    
    heapq.heapify(jobs)
        
    job_queue = []
    
    current_start = 0
    occupied = 0
    turnaround_times = []

    while jobs or job_queue:
        while jobs and jobs[0][0] <= time:
            start, duration = heapq.heappop(jobs)
            heapq.heappush(job_queue, (duration, start))
            if not jobs:
                break
        
        if job_queue and occupied == 0:
            duration, start = heapq.heappop(job_queue)
            occupied = duration
            turnaround_times.append(time - start + duration)
        
        time += 1
        if occupied > 0:
            occupied -= 1
        
    answer = sum(turnaround_times)//len(turnaround_times)
    
    return answer