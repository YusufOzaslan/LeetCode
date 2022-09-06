#include <iostream>
#include <vector>
#include <unordered_map>
#include<algorithm>
using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        if (s.length() == 0)
        {
            return 0;
        }

        vector<int> num;
        vector<char> str = {s[0]};
        int size = s.length();
        int j = 0;
        for (int i = 1; i < size; i++)
        {
            if (!count(str.begin(), str.end(), s[i]))
                str.push_back(s[i]);
            else
            {
                num.push_back(str.size());
                while (count(str.begin(), str.end(), s[i]))
                    str.erase(str.begin());
                str.push_back(s[i]);
            }
        }
        num.push_back(str.size());
        return *max_element(num.begin(), num.end());
    }
};

int main(int argc, char *argv[])
{
    Solution s;
    string test = "pwwqasw";
    cout << s.lengthOfLongestSubstring(test);
    return 0;
}
