class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # right[i] = minimum value from i to n-1
        right = [0] * n
        right[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            right[i] = min(nums[i], right[i + 1])

        # left = maximum value from 0 to i
        left = nums[0]

        for i in range(n):
            left = max(left, nums[i])

            if left - right[i] <= k:
                return i

        return -1