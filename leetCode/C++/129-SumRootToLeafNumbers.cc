/*

Given a binary tree containing digits from 0-9 only,
each root-to-leaf path could represent a curr_num.

An example is the root-to-leaf path 1->2->3 which represents the curr_num 123.
Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the curr_num 12.
The root-to-leaf path 1->3 represents the curr_num 13.

Return the sum = 12 + 13 = 25.

*/



/**
 * Definition for a binary tree node.
 */
#include <iostream>
#include <string>

using namespace std;

struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int sumNumbers(TreeNode* root) {
        /*
            Time:  O(n)
            Space: O(1)
        */
        if (root)
            return sum_number_helper(root, 0);
        return 0;
    }
private:
    int sum_number_helper(TreeNode* root, int curr_num) {
        if (!root)
            return 0;
        if (!(root->left) && !(root->right))
            return 10 * curr_num + root->val;
        return sum_number_helper(root->left, 10 * curr_num + root->val) + sum_number_helper(root->right, 10 * curr_num + root->val);
    }
};

class Solution1 {
public:
    int sumNumbers(TreeNode* root) {
        /*
            Time:  O(n)
            Space: O(1)
        */
        if (root)
            sum_number_helper(root, "");
        return res;
    }
private:
    int res = 0;
    void sum_number_helper(TreeNode* root, string curr_num) {
        if (!root)
            return;
        if (!(root->left) && !(root->right)) {
            res += stoi(curr_num + to_string(root->val));
            return;
        }
        sum_number_helper(root->left, curr_num + to_string(root->val));
        sum_number_helper(root->right, curr_num + to_string(root->val));
    }
};


int main(void) {
    Solution s;
    TreeNode t1(1);
    TreeNode t2(2);
    TreeNode t3(3);
    (&t1)->left = &t2;
    (&t1)->right = &t3;
    cout << s.sumNumbers(&t1) << endl;
    return 0;
};