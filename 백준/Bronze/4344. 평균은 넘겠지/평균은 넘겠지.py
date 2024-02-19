C = int(input())

for _ in range(C):
    N = list(map(int, input().split()))
    amount = N[0]
    total = sum(N) - amount
    average = total/amount

    count = 0 
    for i in range(1,amount+1):
        if N[i] > average:
            count += 1
    print((count/amount)*100,"%")            
        
        