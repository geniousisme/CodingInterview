/*
Remove all elements from a linked list of integers that have value val.
Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        /*
            Time:  O(n)
            Space: O(1)
        */
        ListNode *dummy, *new_start;
        dummy->next = head, new_start = dummy;
        while (dummy->next) {
            if (dummy->next->val == val)
                dummy->next = dummy->next->next;
            else
                dummy = dummy->next;
        }
        return new_start->next;
    }
};