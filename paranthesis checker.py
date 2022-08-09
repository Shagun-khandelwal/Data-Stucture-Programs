# LeetCode 20. valid Paranthesis Checker
def ispar(s):
    stack = []
    for x in s:
        if x == "(" or x == "[" or x == "{":
            stack.append(x)
        elif x in [")", "]", "}"]:
            if not stack:
                return False
            popped = stack.pop()
            if popped == "(":
                if x != ")":
                    return False
            elif popped == "[":
                if x != "]":
                    return False
            elif popped == "{":
                if x != "}":
                    return False
    if len(stack) != 0:
        return False
    else:
        return True

myinput = "{([])}"
print(ispar(myinput))