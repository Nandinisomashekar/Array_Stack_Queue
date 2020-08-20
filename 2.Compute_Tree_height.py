def tree(tree_list, i , d): 
    if d[i] != 0: 
        return 

    if tree_list[i] == -1: 
        d[i] = 1
        return 
  
    if d[tree_list[i]] == 0: 
        tree(tree_list, tree_list[i] , d) 
  
    d[i] = d[tree_list[i]] + 1
    
n = int(input())
tree_list = [int(item) for item in input().split()]
d = [0 for i in range(n)] 
for i in range(n): 
    tree(tree_list, i, d) 
height = d[0] 
for i in range(1,n): 
    height = max(height, d[i]) 
print(height)