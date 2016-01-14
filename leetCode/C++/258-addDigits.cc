class Solution1 { // iterative solution
public:
    int addDigits(int num) {
        int ans = 10;
        while (ans >= 10) {
            ans = 0;
            while (num) {
                ans += num % 10;
                num /= 10;
            }
            num = ans;
        }
        return ans;
    }
};

class Solution {
public:
    int addDigits(int num) {
        if (!num)
            return num;
        return num - 9 * ((num - 1) / 9);
    }
};