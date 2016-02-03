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