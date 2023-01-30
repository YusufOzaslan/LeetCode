from ast import List
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if (x == 0):
            return res
        if (x > 0):
            while (x != 0):
                res = res*10 + x%10
                x = int(x/10)
        else:
            x = -x
            while (x != 0):
                res = res*10 + x%10
                x = int(x/10)
            res = -res
        if (-2**31 <= res <= 2**31 - 1):
            return res
        else:
            return 0
# Test
s = Solution()
print (s.reverse(-1230))