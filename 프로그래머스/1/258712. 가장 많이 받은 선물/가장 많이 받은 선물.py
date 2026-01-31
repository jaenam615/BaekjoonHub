def solution(friends, gifts):
    table = [[0] * len(friends) for _ in range(len(friends))]
    
    present_index = {}
    for friend in friends:
        present_index[friend] = 0
        
    for gift in gifts:
        giver, receiver = gift.split()
        for idx, friend in enumerate(friends):
            if giver == friend:
                first_index = idx
            if receiver == friend:
                second_index = idx
        table[first_index][second_index] += 1
        present_index[giver] += 1
        present_index[receiver] -= 1
        
    answer = 0

    received_presents = [0] * len(friends)
    for i in range(len(received_presents)):
        for j in range(len(received_presents)):
            if table[i][j] > table[j][i]:
                received_presents[i] += 1
            if table[i][j] == table[j][i]:
                if present_index[friends[i]] > present_index[friends[j]]:
                    received_presents[i] += 1
    
    return max(received_presents)