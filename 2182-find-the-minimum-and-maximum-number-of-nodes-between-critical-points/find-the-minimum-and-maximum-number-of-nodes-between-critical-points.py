class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next

        first = -1
        last = -1
        min_dist = float('inf')

        index = 1

        while curr.next:
            # Check whether curr is a critical point
            is_critical = (
                (curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)
            )

            if is_critical:
                # First critical point
                if first == -1:
                    first = index
                    last = index
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, index - last)
                    last = index

            prev = curr
            curr = curr.next
            index += 1

        # Fewer than 2 critical points
        if first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]