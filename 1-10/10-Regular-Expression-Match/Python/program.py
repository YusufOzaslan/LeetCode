# Dynamic programming
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = []
        for i in range(n+1):
            row = [False] * (m+1)
            dp.append(row)
            
        dp[0][0] = True

        for i in range(n+1):
            for j in range(1, m+1):
                if p[j-1] == '.':
                    dp[i][j] = i > 0 and dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (i > 0 and (p[j-2] == '.' or p[j-2] == s[i-1]) and dp[i-1][j])
                else:
                    dp[i][j] = i > 0 and s[i-1] == p[j-1] and dp[i-1][j-1]

        return dp[n][m]

# Test
s = Solution()
print (s.isMatch("aa",".*"))