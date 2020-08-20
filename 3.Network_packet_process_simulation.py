from collections import deque 

[buf_size,no_of_packets] = [int(item) for item in input().split()]
packets = {}
starting_time = {}
for i in range(no_of_packets):
    packets[i+1]= [int(v) for v in input().split()]
    
buffer = deque(maxlen=buf_size)
for i in packets:
    while buffer and buffer[0] <= packets[i][0]:
        buffer.popleft()
        
    if len(buffer) >= buf_size:
        starting_time[i] = -1
    else:
        starting_time[i] = max(packets[i][0], buffer[-1] if buffer else 0)
        buffer.append(starting_time[i] + packets[i][1])
for i in starting_time:
    print(starting_time[i])