#include "include/common.h"
/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
 */
class Solution{
public:
    /**
     * @param head: The first node of linked list.
     * @return: head node
     */
    ListNode *deleteDuplicates(ListNode *head) {
             if (head == nullptr || head->next == nullptr) {
                return head;
             };
             ListNode *start = new ListNode(-999), *prev, *post;
             start->next = head;
             // set two ptrs to record the repeated things happen
             prev = start;
             post = start->next;
             while (prev->next) {
                    // delete the repeated things
                    while(post->next && prev->next->val == post->next->val) {
                        post = post->next;
                    };
                    // not repeated, both move forward
                    if (prev->next == post) {
                        prev = prev->next;
                        post = post->next;
                    } else { // repeated, set prev ptr point to the non-repeated ptr
                        prev->next = post->next;
                    };
             };
             return start->next;           
    }
};


int main(void) {
    Solution s;
    Utils    u;
    ListNode *l1 = new ListNode(1);
    ListNode *l2 = new ListNode(1);
    ListNode *l3 = new ListNode(1);
    ListNode *l4 = new ListNode(2);
    ListNode *l5 = new ListNode(3);
    l1->next = l2;
    l2->next = l3;
    l3->next = l4;
    l4->next = l5;
    u.printLinkedList(s.deleteDuplicates(l1));
    return 0;
}