/*
Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
*/

#include <iostream>

using namespace std;

struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (!head || !(head->next))
            return nullptr;

        ListNode *slow = head, *fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast)
                break;
        }

        if (!fast || !(fast->next))
            return nullptr;

        slow = head;
        while (fast != slow) {
            fast = fast->next;
            slow = slow->next;
        }
        return slow;
    }
};
int main(void) {

    return 0;
};