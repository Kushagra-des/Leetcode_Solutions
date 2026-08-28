from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        odd_chars = [c for c in cnt if cnt[c] % 2 == 1]

        # 1. Can s even form a palindrome permutation?
        if n % 2 == 0:
            if odd_chars:
                return ""
            mid_char = None
        else:
            if len(odd_chars) != 1:
                return ""
            mid_char = odd_chars[0]

        h = n // 2
        half = [0] * 26
        for c, v in cnt.items():
            half[ord(c) - 97] = v // 2

        def build(core: str) -> str:
            rev = core[::-1]
            return core + mid_char + rev if mid_char is not None else core + rev

        best = None

        # 2a. Candidate that mirrors target's own first half exactly.
        T_half = target[:h]
        half_from_T = [0] * 26
        for ch in T_half:
            half_from_T[ord(ch) - 97] += 1

        if half_from_T == half:
            F0 = build(T_half)
            if F0 > target:
                best = F0

        # 2b. Otherwise, find the LARGEST divergence point inside the first half.
        if best is None:
            state = half[:]
            best_j, best_c = -1, -1
            for j in range(h):
                tj = ord(target[j]) - 97
                for ci in range(tj + 1, 26):
                    if state[ci] > 0:
                        best_j, best_c = j, ci
                        break
                if state[tj] > 0:
                    state[tj] -= 1
                else:
                    break

            if best_j != -1:
                state2 = half[:]
                for k in range(best_j):
                    state2[ord(target[k]) - 97] -= 1
                state2[best_c] -= 1

                core_chars = list(target[:best_j])
                core_chars.append(chr(best_c + 97))
                for ci in range(26):
                    core_chars.extend([chr(ci + 97)] * state2[ci])

                best = build(''.join(core_chars))

        return best if best is not None else ""