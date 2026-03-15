class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key = lambda x : x[0])
        dp = [1 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[j] + 1  , dp[i])
        print(dp)
        return max(dp)