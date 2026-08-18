from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {}

        # Count how many times each number appears
        for i in range(n - k + 1):
            window = nums[i:i + k]

            for num in set(window):
                freq[num] = freq.get(num, 0) + 1

        # Find the largest number that appears in exactly one window
        ans = -1

        for num, count in freq.items():
            if count == 1:
                ans = max(ans, num)

        return ans