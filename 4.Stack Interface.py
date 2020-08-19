n = int(input())
operations = []
for i in range(n):        
    oper = input()
    operations.append(oper)
s= []
for op in operations:
    if "push" in op:
        s.append(int(op[5:]))
    if op == "pop":
        s.pop()
    if op == "max":
        print(max(s))