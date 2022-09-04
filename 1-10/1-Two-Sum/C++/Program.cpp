#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> hashMap;
        for (int i = 0; i < nums.size(); i++)
        {
            // int diff target - nums[i]
            if (hashMap.count(target - nums[i]))
                return {hashMap[target - nums[i]], i};
            hashMap[nums[i]] = i;
        }
    }
};

int main(int argc, char *argv[])
{
    Solution s;
    int target = 9;
    vector<int> nums{ 2, 7, 11, 15};
    int size = s.twoSum(nums, target).size();
    cout << "[ ";
    for (int i = 0; i < size; i++)
    {
         cout << s.twoSum(nums, target).at(i) << " ";
    }
    cout << "]";
    return 0;
}
