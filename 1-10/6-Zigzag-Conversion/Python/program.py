class Solution:
    def convert(self, s, numRows):
        if (numRows == 1):
            return s
        zigzagNum = 2*numRows-2
        zigzagStr = ""

        for i in range(numRows):
            for j in range(len(s)):
                if j % zigzagNum == i:
                    zigzagStr += s[j]
                elif j % zigzagNum >= numRows and (j + i*2)%zigzagNum == i:
                    zigzagStr += s[j]

        return zigzagStr

# Test
input = "PAYPALISHIRING"
s = Solution()
print(s.convert(input, 3))