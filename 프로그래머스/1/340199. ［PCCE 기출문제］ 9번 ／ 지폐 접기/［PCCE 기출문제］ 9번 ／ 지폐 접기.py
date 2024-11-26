def fold(arr):
    if arr[0] >= arr[1]:
        arr[0] //= 2
    else: 
        arr[1] //=2 
    
    return arr

def solution(wallet, bill):
    answer = 0
    while 1:
        if (bill[0] <= wallet[0] and bill[1] <= wallet[1]) or (bill[1] <= wallet[0] and bill[0] <= wallet[1]):
            break
        bill = fold(bill)
        answer += 1
    return answer

