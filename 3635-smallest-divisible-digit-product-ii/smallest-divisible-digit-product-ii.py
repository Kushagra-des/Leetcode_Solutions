class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # (exp2, exp3, exp5, exp7) contributed by each digit 0-9
        DP = [
            (0,0,0,0), (0,0,0,0), (1,0,0,0), (0,1,0,0), (2,0,0,0),
            (0,0,1,0), (1,1,0,0), (0,0,0,1), (3,0,0,0), (0,2,0,0),
        ]

        def sub(a, b):
            return (max(0, a[0]-b[0]), max(0, a[1]-b[1]),
                    max(0, a[2]-b[2]), max(0, a[3]-b[3]))

        def factor_count(cnt):
            # minimal digits (2..9) needed to cover required (a,b,c,d)
            a, b, c, d = cnt
            c8, r2 = divmod(a, 3)   # 8 = 2^3
            c9, r3 = divmod(b, 2)   # 9 = 3^2
            c4, c2 = divmod(r2, 2)  # leftover 2's: use a 4 or a 2
            c3 = r3                 # leftover single 3
            c6 = 0
            if c2 == 1 and c3 == 1:      # merge lone 2 + lone 3 -> one 6 (saves a digit)
                c2 = c3 = 0
                c6 = 1
            if c3 == 1 and c4 == 1:      # swap {3,4} -> {2,6} (same length, smaller digits)
                c2, c6, c3, c4 = 1, 1, 0, 0
            return (c2, c3, c4, c, c6, d, c8, c9)  # counts for digits 2,3,4,5,6,7,8,9

        def construct(fc):
            digits = "23456789"
            return "".join(ch * cnt for ch, cnt in zip(digits, fc))

        # factor t into primes 2,3,5,7; anything left over -> impossible
        a = b = c = d = 0
        tmp = t
        while tmp % 2 == 0: tmp //= 2; a += 1
        while tmp % 3 == 0: tmp //= 3; b += 1
        while tmp % 5 == 0: tmp //= 5; c += 1
        while tmp % 7 == 0: tmp //= 7; d += 1
        if tmp != 1:
            return "-1"
        req = (a, b, c, d)

        fc = factor_count(req)
        n = len(num)
        if sum(fc) > n:
            return construct(fc)  # num is too short; use the minimal-length answer

        prefix = [0, 0, 0, 0]
        first_zero = -1
        for i, ch in enumerate(num):
            dg = ord(ch) - 48
            if dg == 0:
                if first_zero == -1:
                    first_zero = i
                continue
            e = DP[dg]
            prefix[0] += e[0]; prefix[1] += e[1]; prefix[2] += e[2]; prefix[3] += e[3]
        prefix = tuple(prefix)

        if first_zero == -1:
            first_zero = n
            if all(prefix[k] >= req[k] for k in range(4)):
                return num  # num itself already works

        for i in range(n - 1, -1, -1):
            dg = ord(num[i]) - 48
            prefix = sub(prefix, DP[dg])       # prefix now = digits before i
            space = n - 1 - i
            if i > first_zero:
                continue                       # can't keep a zero digit in the prefix
            base = sub(req, prefix)
            for bigger in range(dg + 1, 10):
                remaining = sub(base, DP[bigger])
                fac = factor_count(remaining)
                needed = sum(fac)
                if needed <= space:
                    fill = space - needed
                    return num[:i] + str(bigger) + "1" * fill + construct(fac)

        # no same-length fix; go one digit longer
        fac_ext = factor_count(req)
        return "1" * (n + 1 - sum(fac_ext)) + construct(fac_ext)