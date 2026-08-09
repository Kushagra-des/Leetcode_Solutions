class Solution:
    def convert(self, s, numRows):
        # If there is only one row, there is no zigzag
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        current_row = 0
        direction = 1

        for ch in s:
            rows[current_row] += ch

            # Change direction at the top and bottom
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        return "".join(rows)