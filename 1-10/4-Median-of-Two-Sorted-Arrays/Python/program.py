# time complexity: O(n), space complexity: O(n)
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        firstPointer = 0
        secondPointer = 0
        mergedList = []
        
        while firstPointer < len(nums1) and secondPointer < len(nums2):
            if nums1[firstPointer] < nums2[secondPointer]:
                mergedList.append(nums1[firstPointer])
                firstPointer += 1
            else:
                mergedList.append(nums2[secondPointer])
                secondPointer += 1
                
        while firstPointer < len(nums1):
            mergedList.append(nums1[firstPointer])
            firstPointer += 1
            
        while secondPointer < len(nums2):
            mergedList.append(nums2[secondPointer])
            secondPointer += 1
        if len(mergedList)%2 == 1:
            return mergedList[len(mergedList)//2]
        else:
            return (mergedList[len(mergedList)//2 - 1] + mergedList[len(mergedList)//2]) / 2

#Test
nums1 = [1,3]
nums2 = [2]
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))