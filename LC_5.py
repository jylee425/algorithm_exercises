class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        res = s[0]
        
        memo = [[0] * N for _ in range(N)]
        for i in range(N):
            memo[i][i] = 1
        
        for i in range(N):
            for j in range(i):
                if s[i]==s[j] and (memo[j+1][i-1] or i==j+1):
                    memo[j][i] = 1
                    if i-j+1 >= len(res):
                        res = s[j:i+1]
        
        return res
