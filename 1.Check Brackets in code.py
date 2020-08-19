S = input()
def check_parentheses(S):
    brackets = {"(": ")", "[": "]",  "{": "}"}
    open_brackets = ['(','[','{']
    stack = []
    special_char = [":",";","/","#","@","!","$","%","^","&","*"]
    for bracket in S:
        if 122>=ord(bracket)>=97 or 90>=ord(bracket)>=65 or 57>=ord(bracket)>=48 or bracket in special_char:
            continue
        elif bracket in open_brackets:
            stack.append(bracket)
        elif stack and bracket == brackets[stack[-1]]:
                stack.pop()
        else:
            return False
    return stack == []
if check_parentheses(S):
    print("Success")
else:
    print("1")
