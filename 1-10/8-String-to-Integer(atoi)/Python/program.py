from ast import List
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        length, res, sign, itr = len(s), 0, 1, 0
        if length == 0:
            return res

        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        for e in s:
            if e.isdigit():
                res = res*10 + ord(e) - ord("0")
            else:
                break

        if sign < 0:
            res = sign*res

        if -2**31 <= res <= 2**31 - 1:
            return res
        elif res >= 2**31 - 1:
            return 2**31 - 1
        else:
            return -2**31

# Test
s = Solution()
print (s.myAtoi(" -3.42"))