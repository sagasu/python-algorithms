class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        ans = [-1] * N

        for _, index in sorted((rating, index) for index, rating in enumerate(ratings)):
            current = 1

            if index - 1 >= 0 and ratings[index] > ratings[index - 1]:
                current = max(current, ans[index - 1] + 1)
            if index +1 < N and ratings[index] > ratings[index + 1]:
                current = max(current, ans[index + 1] + 1)
            ans[index] = current
        return sum(ans)