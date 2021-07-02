class Solution:
    def findClosestElements(self, arr: List[int], k: int, target: int) -> List[int]:
        N = len(arr)
        index = bisect.bisect_left(arr, target)

        left = index -1
        right = index
        results = collections.deque()

        while len(results) < k and left >= 0 and right < N:
            if target- arr[left] <= arr[right] - target:
                results.appendleft(arr[left])
                left -= 1
            else:
                results.append(arr[right])
                right += 1

        while len(results) < k and left >= 0:
            results.appendleft(arr[left])
            left -= 1
        while len(results) < k and right < N:
            results.append(arr[right])
            right += 1

        return results