class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Rows with no reserved seats can accommodate 2 families each.
        ans = 2 * n

        # Store reserved seats only for rows that matter.
        rows = {}

        for r, seat in reservedSeats:
            if seat in (2, 3, 4, 5, 6, 7, 8, 9):
                rows[r] = rows.get(r, 0) | (1 << seat)

        # Masks for the three possible 4-seat blocks.
        left = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        middle = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        right = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

        for mask in rows.values():
            # This row is not completely empty anymore.
            ans -= 2

            if (mask & left) == 0 and (mask & right) == 0:
                # Both outer groups can be used.
                ans += 2
            elif (mask & left) == 0 or (mask & middle) == 0 or (mask & right) == 0:
                # At least one group can be used.
                ans += 1

        return ans