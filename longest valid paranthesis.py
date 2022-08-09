#Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring
<<<<<<< HEAD
=======

>>>>>>> 08c0ddfc227f7d24ecd9b470a64474d53e76f30b
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
