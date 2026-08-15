class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()

        n = len(nums)

        # Initial answer using the first three elements
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]

                # Exact match
                if current == target:
                    return current

                # Update closest answer
                if abs(current - target) < abs(closest - target):
                    closest = current

                # Adjust pointers
                if current < target:
                    left += 1
                else:
                    right -= 1

        return closest