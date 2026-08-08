from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        ans = [0] * m
        last = [-1] * m  # last[j] = earliest i such that word2[j:] is a subsequence of word1[i:]

        # Backward pass: build `last` by matching word2 as a subsequence of word1 from the right
        i, j = n - 1, m - 1
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        # Forward greedy pass with one allowed mismatch
        can_skip = True
        j = 0
        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                ans[j] = i
                j += 1
            elif can_skip and (j == m - 1 or i < last[j + 1]):
                # Spend our one mismatch here — still feasible to finish the rest
                can_skip = False
                ans[j] = i
                j += 1

        return ans if j == m else []