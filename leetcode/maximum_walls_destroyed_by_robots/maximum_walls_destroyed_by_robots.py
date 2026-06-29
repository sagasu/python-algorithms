from typing import List
import bisect


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        walls.sort()
        n = len(robots)
        bots = sorted(zip(robots, distance))

        def count(lo: int, hi: int) -> int:
            if lo > hi:
                return 0
            return bisect.bisect_right(walls, hi) - bisect.bisect_left(walls, lo)

        if n == 1:
            pos, dist = bots[0]
            return max(count(pos - dist, pos), count(pos, pos + dist))

        # For each robot i (sorted), define:
        #   left_i  = walls robot i hits firing LEFT  (blocked by robot i-1 at prev_pos)
        #             range: [max(pos-dist, prev_pos+1), pos]
        #   right_i = walls robot i hits firing RIGHT (blocked by robot i+1 at next_pos)
        #             range: [pos, min(pos+dist, next_pos-1)]
        #
        # The gap between robot i and robot i+1 is (pos_i, pos_{i+1}).
        # Walls in this gap can be covered by:
        #   - robot i firing RIGHT:  [pos_i, min(pos_i+dist_i, pos_{i+1}-1)]
        #   - robot i+1 firing LEFT: [max(pos_{i+1}-dist_{i+1}, pos_i+1), pos_{i+1}]
        # These two ranges may OVERLAP in the gap, so we must not double-count.
        #
        # Define gap_walls(i) = walls strictly between robot i and robot i+1
        #   right_only(i) = walls only robot i's right bullet reaches (not robot i+1's left)
        #   left_only(i+1) = walls only robot i+1's left bullet reaches (not robot i's right)
        #   both(i) = walls both can reach
        #
        # Transitions from robot i to robot i+1:
        #   prev=LEFT,  curr=LEFT:  dp_a + left_{i+1}
        #   prev=LEFT,  curr=RIGHT: dp_a + right_{i+1}
        #   prev=RIGHT, curr=LEFT:  dp_b + left_{i+1} - overlap(i, i+1)
        #     (dp_b already counted right_i which may overlap with left_{i+1})
        #   prev=RIGHT, curr=RIGHT: dp_b + right_{i+1}
        #     (right_i and right_{i+1} are disjoint since robot i+1 blocks right_i)

        pos0, dist0 = bots[0]
        pos1 = bots[1][0]

        dp_a = count(pos0 - dist0, pos0)
        dp_b = count(pos0, min(pos0 + dist0, pos1 - 1))

        for i in range(1, n):
            pos, dist = bots[i]
            prev_pos, prev_dist = bots[i - 1]
            next_pos = bots[i + 1][0] if i + 1 < n else pos + dist + 1

            left  = count(max(pos - dist, prev_pos + 1), pos)
            right = count(pos, min(pos + dist, next_pos - 1))

            # Overlap: walls that both prev's right bullet AND curr's left bullet cover
            # prev right range: [prev_pos, min(prev_pos+prev_dist, pos-1)]
            # curr left range:  [max(pos-dist, prev_pos+1), pos]
            # overlap is in the gap (prev_pos, pos) exclusive of robots:
            overlap_lo = max(prev_pos + 1, pos - dist)
            overlap_hi = min(prev_pos + prev_dist, pos - 1)
            overlap = count(overlap_lo, overlap_hi)

            new_a = max(dp_a + left, dp_b + left - overlap)
            new_b = max(dp_a + right, dp_b + right)

            dp_a, dp_b = new_a, new_b

        return max(dp_a, dp_b)
