class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # 1. Remove both from the left
        remove_left = right + 1

        # 2. Remove both from the right
        remove_right = n - left

        # 3. Remove one from each side
        remove_both = (left + 1) + (n - right)

        return min(remove_left, remove_right, remove_both)