#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int expected_sum = ((nums.size() + 1) * nums.size()) / 2;
        int real_sum = 0;
        for (const auto &num: nums)
            real_sum += num;
        return expected_sum - real_sum;
    }
};

int main(void) {
    Solution s;
    vector<int> nums {0, 1, 2, 3, 4, 5, 7};
    cout << s.missingNumber(nums) << endl;
    return 0;
}