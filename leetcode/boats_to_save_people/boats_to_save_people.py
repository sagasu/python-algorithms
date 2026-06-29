class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        
        heaviest = len(people) - 1
        lightest = 0
        
        while heaviest > lightest:
            if people[heaviest] + people[lightest] <= limit:
                lightest += 1
            heaviest -= 1
            boats += 1
            
        if heaviest == lightest:
            boats += 1
        
        return boats