from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        # Give every litter cell a bit index.
        litter_id = [[-1] * n for _ in range(m)]

        start_r = start_c = 0
        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c

                elif classroom[r][c] == 'L':
                    litter_id[r][c] = litter_count
                    litter_count += 1

        # Nothing to clean.
        if litter_count == 0:
            return 0

        # All litter initially remains.
        all_mask = (1 << litter_count) - 1

        # State:
        # (row, col, remaining_energy, mask)
        queue = deque()
        queue.append((start_r, start_c, energy, all_mask))

        # Store visited states.
        visited = set()
        visited.add((start_r, start_c, energy, all_mask))

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        moves = 0

        while queue:
            for _ in range(len(queue)):
                r, c, cur_energy, mask = queue.popleft()

                # All litter has been collected.
                if mask == 0:
                    return moves

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside the grid.
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    # Obstacle.
                    if classroom[nr][nc] == 'X':
                        continue

                    # Cannot move if we have no energy.
                    if cur_energy == 0:
                        continue

                    # One move costs one energy.
                    new_energy = cur_energy - 1
                    new_mask = mask

                    # Collect litter.
                    if classroom[nr][nc] == 'L':
                        bit = litter_id[nr][nc]
                        new_mask &= ~(1 << bit)

                    # Reset energy when reaching R.
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    state = (nr, nc, new_energy, new_mask)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            moves += 1

        return -1