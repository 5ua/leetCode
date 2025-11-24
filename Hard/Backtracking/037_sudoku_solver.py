from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """®
        Solve the Sudoku puzzle in-place using backtracking with bitmasks and MRV heuristic.
        - Each row/col/box keeps a 9-bit mask of used digits.
        - At each step, pick the empty cell with the fewest candidates (MRV) to reduce branching.
        Time: Backtracking (typically very fast with MRV); Space: O(1) aux (fixed-size masks).
        """

        N = 9
        FULL = (1 << 9) - 1  # 0b1_1111_1111, all digits available
        rows = [0] * N       # rows[r] bit d set => digit (d+1) used in row r
        cols = [0] * N
        boxes = [0] * N

        def box_id(r: int, c: int) -> int:
            return (r // 3) * 3 + (c // 3)

        empties = []

        # Initialize masks from the given board and collect empty cells
        for r in range(N):
            for c in range(N):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    d = ord(board[r][c]) - ord('1')  # 0..8
                    bit = 1 << d
                    b = box_id(r, c)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[b] |= bit

        def candidates_mask(r: int, c: int) -> int:
            """Return bitmask of digits allowed at (r,c)."""
            used = rows[r] | cols[c] | boxes[box_id(r, c)]
            return (~used) & FULL

        def place(r: int, c: int, d: int) -> None:
            """Place digit d (0..8) at (r,c) and set masks."""
            bit = 1 << d
            rows[r] |= bit
            cols[c] |= bit
            boxes[box_id(r, c)] |= bit
            board[r][c] = chr(ord('1') + d)

        def remove(r: int, c: int, d: int) -> None:
            """Remove digit d (0..8) from (r,c) and unset masks."""
            bit = 1 << d
            rows[r] ^= bit
            cols[c] ^= bit
            boxes[box_id(r, c)] ^= bit
            board[r][c] = '.'

        def choose_mrv(idx_list) -> int:
            """
            Among indices in `idx_list` (positions in `empties`), pick the index with min candidates.
            Returns the position in the list (not the (r,c) tuple).
            """
            best_pos = 0
            best_count = 10
            for pos, k in enumerate(idx_list):
                r, c = empties[k]
                mask = candidates_mask(r, c)
                cnt = mask.bit_count()
                if cnt < best_count:
                    best_count = cnt
                    best_pos = pos
                    if cnt == 1:  # cannot do better than 1
                        break
            return best_pos

        # We'll mutate a list of indices to empties to avoid shuffling the main array
        idxs = list(range(len(empties)))

        def dfs() -> bool:
            # If no empties left, solved
            if not idxs:
                return True

            # Pick MRV cell (fewest candidates)
            p = choose_mrv(idxs)
            idxs[p], idxs[-1] = idxs[-1], idxs[p]  # move chosen to end
            k = idxs.pop()
            r, c = empties[k]

            mask = candidates_mask(r, c)
            # Try each candidate bit
            while mask:
                bit = mask & -mask         # lowest set bit
                d = bit.bit_length() - 1   # digit 0..8
                place(r, c, d)
                if dfs():
                    return True
                remove(r, c, d)
                mask ^= bit

            # Backtrack: restore index
            idxs.append(k)
            return False

        dfs()
