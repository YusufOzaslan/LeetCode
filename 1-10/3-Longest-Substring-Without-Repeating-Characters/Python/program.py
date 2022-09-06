class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        strList = []
        strList.append(s[0])
        numList = []        
        
        for i in range(1, len(s)):
            if s[i] not in strList:
                strList.append(s[i])
            else:
                numList.append(len(strList))
                j = 0
                while s[i] in strList:
                    strList.pop(j)
                strList.append(s[i])

        numList.append(len(strList))
        return max(numList)

#Test
test = "pwwqasw"
s = Solution()
print(s.lengthOfLongestSubstring(test))