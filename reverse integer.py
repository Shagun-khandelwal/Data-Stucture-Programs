# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

def reverse(x: int) -> int:
    negative = False
    if x < 0:
        negative = True
        x = -x
    newnum = 0
    while x != 0:
        val = x % 10
        newnum = newnum * 10 + val
        x //= 10
    if negative:
        newnum = -newnum
    if newnum > 2 ** 31 - 1 or newnum < -2 ** 31:
        return 0
    return newnum
print(reverse(-123))