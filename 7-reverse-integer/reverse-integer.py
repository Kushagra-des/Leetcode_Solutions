class Solution:
    def reverse(self, x):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_num = 0

        while x > 0:
            digit = x % 10
            x //= 10

            reversed_num = reversed_num * 10 + digit

        reversed_num *= sign

        # Check 32-bit signed integer range
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num