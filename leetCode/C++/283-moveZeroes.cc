#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void moveZeroes1(vector<int>& nums) { // with swap
        // Time:  O(n)
        // Space: O(1)
        int non_zero_index = 0, index = 0;
        while (index < nums.size()) {
            if (nums[index] != 0) {
                swap(nums, non_zero_index, index);
                non_zero_index++;
            }
            index++;
        }
    }
    void moveZeroes(vector<int>& nums) { // with writing array directly
        // Time:  O(n)
        // Space: O(1)
        int zero_start_index = 0;
        for (auto it = nums.begin(); it != nums.end(); ++it) {
            if (*it) {
                nums[zero_start_index] = *it;
                zero_start_index++;
            }
        }
        for (int i = zero_start_index; i < nums.size(); ++i)
            nums[i] = 0;
    }
private:
    void swap(vector<int>& nums, int index1, int index2) {
        int tmp = nums[index1];
        nums[index1] = nums[index2];
        nums[index2] = tmp;
    }
    void print_vector(vector<int>& nums) {
        for (const auto &num: nums)
            cout << num << " ";
        cout << endl;
    }
};

int main(void) {
    // int arr[] = {1, 2, 3, 0, 0, 0, 4, 0, 5};
    Solution s;
    vector<int> nums {1, 2, 3, 0, 0, 0, 4, 0, 5};
    s.moveZeroes(nums);
    return 0;
}