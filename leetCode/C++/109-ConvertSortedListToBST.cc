#include "include/common.h"
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
      ListNode *dummy = head;
      int length = 0;
      while (dummy) {
        dummy = dummy->next;
        length++;
      };
      return buildBST(head, 0, length - 1);
    }
private:
    TreeNode* buildBST(ListNode *&head, int start, int end) {
      if (start > end)
        return nullptr;
      int mid = (start + end) / 2;
      TreeNode *leftTree = buildBST(head, start, mid - 1);
      TreeNode *root = new TreeNode(head->val);
      head = head->next;
      TreeNode *rightTree = buildBST(head, mid + 1, end);
      root->left = leftTree;
      root->right = rightTree;
      return root;
    }
};  