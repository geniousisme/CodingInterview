#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if (nums.size() == 0)
            return;
        k %= nums.size();
        reverse(nums, 0, nums.size() - k - 1);
        reverse(nums, nums.size() - k, nums.size() - 1);
        reverse(nums, 0, nums.size() - 1);
    }
private:
    void reverse(vector<int>& nums, int start, int end) {
        while (start < end) {
            int tmp = nums[start];
            nums[start] = nums[end];
            nums[end] = tmp;
            start++;
            end--;
        }
    }
};

int main(void) {
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    Solution s;
    s.rotate(nums, 10);
    for (const auto &num: nums)
        cout << num << " ";
    cout << endl;
};