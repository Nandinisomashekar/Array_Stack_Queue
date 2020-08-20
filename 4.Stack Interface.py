n = int(input()) 
operations = []
for i in range(n):        
    oper = input()
    operations.append(oper)

Stack = []
MaxStack = []

for op in operations:
    if "push" in op:
        x = int(op[5:])
        Stack.append(x)  
        if (len(Stack) == 1): 
            MaxStack.append(x)
            continue
        if (x > MaxStack[-1]):  
            MaxStack.append(x)  
        else: 
            MaxStack.append(MaxStack[-1]) 
  
    if op == "pop":
        Stack.pop()  
        MaxStack.pop()
        
    if op == "max":
        print(MaxStack[-1])
