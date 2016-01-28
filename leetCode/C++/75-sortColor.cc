/*
Given an array with n objects colored red,
white or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red,
white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int count[3] = {0};
        for (const auto &num: nums)
            ++count[num];
        int i = 0, count_i = 0;
        while (i < nums.size()) {
            while (count[count_i] > 0) {
                count[count_i] -= 1;
                nums[i] = count_i;
                ++i;
            }
            count_i += 1;
        }
    }
};


// class Solution {
// };

int main(void) {
    Solution s;
    // vector<int> nums {0, 1, 0, 0, 1, 1, 1, 2, 0, 1, 0, 2, 1, 2};
    vector<int> nums {1, 0};

    s.sortColors(nums);
    for (const auto &num: nums)
        cout << num << " ";
    cout << endl;
    return 0;
};