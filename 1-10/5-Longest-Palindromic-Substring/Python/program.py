"""
class Solution:
    def longestPalindrome(self, s: str) -> str:

        lenS = len(s)
        plndrmcSubstr = ""

        for i in range(lenS):
            lptr, rptrOdd, rptrEven = i, i, i+1
            checkOdd, checkEven = True, True
            while lptr >= 0:
                if rptrOdd < lenS:
                    if (rptrOdd - lptr + 1) > len(plndrmcSubstr) and s[lptr] == s[rptrOdd] and checkOdd:
                        plndrmcSubstr = s[lptr:rptrOdd+1]
                    elif s[lptr] != s[rptrOdd]:
                        checkOdd = False
                if rptrEven < lenS:
                    if (rptrEven - lptr + 1) > len(plndrmcSubstr) and s[lptr] == s[rptrEven] and checkEven:
                        plndrmcSubstr = s[lptr:rptrEven+1]
                    elif s[lptr] != s[rptrEven]:
                        checkEven = False
                rptrOdd += 1
                lptr -= 1
                rptrEven += 1
        return plndrmcSubstr
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:

        lenS = len(s)
        plndrmcSubstr = ""

        for i in range(lenS):
            lptr, rptrOdd = i, i
            while lptr >= 0 and rptrOdd < lenS  and s[lptr] == s[rptrOdd]:
                if (rptrOdd - lptr + 1) > len(plndrmcSubstr):
                    plndrmcSubstr = s[lptr:rptrOdd+1]
                rptrOdd += 1
                lptr -= 1
            lptr, rptrEven = i, i+1
            while lptr >= 0 and rptrEven < lenS and s[lptr] == s[rptrEven]:
                if (rptrEven - lptr + 1) > len(plndrmcSubstr):
                    plndrmcSubstr = s[lptr:rptrEven+1]
                lptr -= 1
                rptrEven += 1
        return plndrmcSubstr

# Test
input = "cbbsbdbsbsb"
s = Solution()
print(s.longestPalindrome(input))