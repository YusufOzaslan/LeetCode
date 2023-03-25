from ast import List
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        else:
            reversed = 0
            temp = x
            while temp != 0:
                reversed = reversed*10 + temp%10
                temp = int(temp/10)
                print(reversed)
            return x == reversed

# Test
s = Solution()
print (s.isPalindrome(12321))