class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        exponent = 0    
        sum = 0
        while (l1 is not None or l2 is not None):
            if (l1 is None):
                sum +=  (l2.val) * pow(10,exponent)
                l2 = l2.next
            elif (l2 is None):
                sum +=  (l1.val) * pow(10,exponent)
                l1 = l1.next
            else:
                sum +=  (l1.val + l2.val) * pow(10,exponent)
                l1 = l1.next
                l2 = l2.next
            exponent += 1 
        
        strSum = str(sum)
        length = len(strSum)
        root = ListNode(int(strSum[length-1]))
        iter = root
        for i in range(length - 2, -1, -1):
            node = ListNode(int(strSum[i]))
            iter.next = node
            iter = node
        return root
# Test
l3 = ListNode(3)
l2 = ListNode(4, l3)
l1 = ListNode(2, l2)
l6 = ListNode(4)
l5 = ListNode(6, l6)
l4 = ListNode(5, l5)
s = Solution()
testNode = s.addTwoNumbers(l1, l4)
while (testNode is not None): 
    print(testNode.val, " ")
    testNode = testNode.next