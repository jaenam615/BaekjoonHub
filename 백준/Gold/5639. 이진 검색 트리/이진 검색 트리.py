#이진검색트리

import sys
sys.setrecursionlimit(10**6)

#입력값 배열에 삽입
A = []
while True:
    try: 
        x = int(sys.stdin.readline())
        A.append(x)
    except:
        break

#후위순회로 바꾸기
#배열의 길이가 0이면 리턴
def postorder(arr):
    if len(arr) ==0:
        return

#전위순회 배열의 첫 값은 루트
    root = arr[0]
    sub_left, sub_right = [], []

#루트보다 작은 값은 왼쪽 서브트리, 큰 값은 오른족 서브트리 배열에 나눈다
    for i in range(1,len(arr)):
        if arr[i] < root:
            sub_left.append(arr[i])
        else:
            sub_right.append(arr[i])

#LRD 순서에 따라 출력    
    postorder(sub_left)
    postorder(sub_right)
    print(root)

postorder(A)
        
    



        