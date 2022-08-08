def maxLength(S):
    # code here
    stack = [0]
    longest = 0
    for x in S:
        if x == "(":
            stack.append(0)
        else:
            if len(stack) > 1:
                val = stack.pop()
                stack[-1] = stack[-1] + val + 2
                longest = max(longest, stack[-1])
            else:
                stack = [0]
    return longest

myinput="(())()("
print(maxLength(myinput))