class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = collections.defaultdict(list)
        for i in range(1, len(arr)):
            res[abs(arr[i]-arr[i-1])].append(sorted([arr[i], arr[i-1]]))
        return sorted(res[min(res)])