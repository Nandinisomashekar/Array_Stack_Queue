from collections import deque 

n= int(input())
arr = [int(item) for item in input().split()]
k= int(input())
Dq = deque() 
for i in range(k): 
    while Dq and arr[i] >= arr[Dq[-1]] : 
        Dq.pop()
    Dq.append(i)

for i in range(k, n): 
    print(str(arr[Dq[0]]) + " ", end = "") 
    while Dq and Dq[0] <= i-k: 
        Dq.popleft()  
    while Dq and arr[i] >= arr[Dq[-1]] : 
        Dq.pop() 
    Dq.append(i) 
print(str(arr[Dq[0]]))