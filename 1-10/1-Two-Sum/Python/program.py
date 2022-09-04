from ast import List
class Solution:
    def twoSum(self, nums, target):
        hashMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[num] = i

if __name__ == '__main__':
    s = Solution()
    print (s.twoSum([2, 7, 11, 15], 9))