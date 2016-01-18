#include <algorithm>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution1 {
public:
    bool isAnagram(string s, string t) {
        /*
            Time:  O(nlogn)
            Space: O(1)
        */
         if (s.length() != t.length())
             return false;
         sort(s.begin(), s.end());
         sort(t.begin(), t.end());
         return s == t;
    }
};

class Solution {
public:
    bool isAnagram(string s, string t) {
        /*
            Time:  O(n)
            Space: O(n)
        */
         unordered_map<char, int> count;
         if (s.length() != t.length())
             return false;
         for (const auto &c: s)
            ++count[tolower(c)];
         for (const auto &c: t) {
            --count[tolower(c)];
            if (count[tolower(c)] < 0)
                return false;
        }
         return true;
    }
};


int main(void) {
    Solution s;
    string test1 = "bdac", test2 = "abcd";
    cout << s.isAnagram(test1, test2) << endl;
    test1 = "car", test2 = "rat";
    cout << s.isAnagram(test1, test2) << endl;
    return 0;
};