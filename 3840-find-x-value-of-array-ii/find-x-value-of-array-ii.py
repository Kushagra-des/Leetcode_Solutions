from typing import List


class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(nums)

        # tree[node] = [product % k, counts of prefix products]
        #
        # tree[node][0] -> product of the whole segment modulo k
        # tree[node][1][r] -> number of prefixes of this segment
        #                  whose product % k == r

        tree = [(1, [0] * k) for _ in range(4 * n)]

        def merge(left, right):
            left_prod, left_cnt = left
            right_prod, right_cnt = right

            prod = (left_prod * right_prod) % k
            cnt = left_cnt[:]

            # A prefix that enters the right segment already
            # contains the entire left segment.
            for r in range(k):
                cnt[(left_prod * r) % k] += right_cnt[r]

            return prod, cnt

        def build(node, l, r):
            if l == r:
                value = nums[l] % k

                cnt = [0] * k
                cnt[value] = 1

                tree[node] = (value, cnt)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, value):
            if l == r:
                value %= k

                cnt = [0] * k
                cnt[value] = 1

                tree[node] = (value, cnt)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            # Completely outside the query range
            if qr < l or r < ql:
                # Identity segment:
                # product = 1
                # no non-empty prefixes
                return 1 % k, [0] * k

            # Completely inside
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # This update persists for all future queries.
            update(1, 0, n - 1, index, value)

            # We need all non-empty prefixes of nums[start:].
            _, cnt = query(1, 0, n - 1, start, n - 1)

            answer.append(cnt[x])

        return answer