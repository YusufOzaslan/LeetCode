using namespace std;
#include <iostream>
#include <string> 
struct ListNode {
	int val;
	ListNode* next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode* next) : val(x), next(next) {}

};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        ListNode root(0);
        ListNode* iter = &root;

        int carry = 0;
        int v1 = l1->val, v2 = l2->val;

        while(carry != 0 || l1 != nullptr || l2 != nullptr){
            if (l1 != nullptr)
               v1 = l1->val;
            else
                v1 = 0;

            if (l2 != nullptr)
               v2 = l2->val;
            else
                v2 = 0;            
            ListNode* node = new ListNode((v1 + v2 + carry) % 10);
            iter->next = node;
            iter = node;            
            carry = (v1 + v2 + carry) / 10;
            
            if(l1 != nullptr) 
                l1 = l1->next;
            if(l2 != nullptr) 
                l2 = l2->next;
        }
        return root.next;
    }
};

int main()
{
	ListNode l3(3);
	ListNode l2(4, &l3);
	ListNode l1(2, &l2);
	ListNode l6(4);
	ListNode l5(6, &l6);
	ListNode l4(5, &l5);
	Solution s = Solution();
	ListNode* testNode = s.addTwoNumbers(&l1, &l4);
	while (testNode != nullptr) {
		cout << testNode->val << " ";
		testNode = testNode->next;
	}
}