S = input()
def check_parentheses(S):
    brackets = {"(": ")", "[": "]",  "{": "}"}
    open_brackets = ['(','[','{']
    stack = []
    for bracket in S:
        if bracket in open_brackets:
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