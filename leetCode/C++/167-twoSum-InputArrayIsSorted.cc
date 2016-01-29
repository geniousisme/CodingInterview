/*
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such
that they add up to the target, where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int start = 0, end = numbers.size() - 1;
        vector<int> res;
        while (start < end) {
            int sum = numbers[start] + numbers[end];
            if (sum < target)
                start += 1;
            else if (sum > target)
                end -= 1;
            else {
                res.push_back(start + 1);
                res.push_back(end + 1);
                break;
            }
        }
        return res;
    }
};

int main(void) {
    Solution s;
    vector<int> numbers {2, 7, 11, 15};
    vector<int> res = s.twoSum(numbers, 9);
    cout << res[0] << " " << res[1] << endl;
    return 0;
}