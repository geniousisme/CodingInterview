#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0, count = 0;
        for (const auto &num: nums) {
            if (count == 0) {
                count = 1;
                candidate = num;
            }
            else if (candidate == num)
                count++;
            else
                count--;
        }
        return candidate;
    }
};

int main(void) {
    Solution s;
    int arr [] = {1, 2, 1, 1, 0, 1};
    vector<int> test(arr, arr + 6);
    cout << s.majorityElement(test) << endl;
    return 0;
};