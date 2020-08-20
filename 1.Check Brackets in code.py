S = input()
brackets = {"(": ")", "[": "]",  "{": "}"}
open_brackets = ['(','[','{']
stack = []
special_char = [":",";","/","#","@","!","$","%","^","&","*"]
for index,bracket in enumerate(S):
    if 122>=ord(bracket)>=97 or 90>=ord(bracket)>=65 or 57>=ord(bracket)>=48 or bracket in special_char:
        continue
    elif bracket in open_brackets:
        stack.append(bracket)
    elif stack and bracket == brackets[stack[-1]]:
            stack.pop()
    else:
        print(index+1)
        
if len(stack)==0:
    print("Success")
