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