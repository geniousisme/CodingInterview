#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int val_start_index = 0;
        for (const auto &num: nums) {
            if (num != val)
                nums[val_start_index++] = num;
        }
        return val_start_index;
    }
};

int main(void) {
    Solution s;
    vector<int> nums {1, 2, 4, 3, 4, 5, 4, 6};
    cout << s.removeElement(nums, 4) << endl;
    return 0;
};