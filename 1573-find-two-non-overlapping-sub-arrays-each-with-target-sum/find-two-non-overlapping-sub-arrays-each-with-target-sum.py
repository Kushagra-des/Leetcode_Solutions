class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')

        # best[i] = minimum length of a target-sum subarray
        # contained entirely in arr[:i]
        best = [INF] * (n + 1)

        # prefix_sum -> latest prefix index
        prefix_index = {0: 0}

        prefix = 0
        ans = INF

        for i in range(1, n + 1):
            prefix += arr[i - 1]

            best[i] = best[i - 1]

            # If prefix[j] = prefix[i] - target,
            # then arr[j:i] has sum == target
            if prefix - target in prefix_index:
                j = prefix_index[prefix - target]
                length = i - j

                # First subarray must lie completely before j
                if best[j] != INF:
                    ans = min(ans, best[j] + length)

                best[i] = min(best[i], length)

            # Latest index gives shortest future subarray
            prefix_index[prefix] = i

        return -1 if ans == INF else ans