class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peaks = 0
        N = len(arr)
        if N <= 2:
            return False

        for index in range(1, N -1):
            if arr[index-1] == arr[index]:
                return False
            if arr[index-1] < arr[index] and arr[index] > arr[index+1]:
                peaks += 1

        if arr[0] >= arr[1]:
            return False
        if arr[-1] >= arr[-2]:
            return False

        return peaks == 1