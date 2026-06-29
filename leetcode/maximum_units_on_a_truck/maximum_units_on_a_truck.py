class Solution:
    def maximumUnits(self, _boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = _boxTypes[:]
        boxTypes.sort(key=lambda item:item[1], reverse = True)

        total = 0
        for boxCount, boxUnits in boxTypes:
            used = min(truckSize, boxCount)
            truckSize -= used
            total += used * boxUnits
        return total