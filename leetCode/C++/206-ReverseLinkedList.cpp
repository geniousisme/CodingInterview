#include <iostream>

using namespace std;

/**
 * Definition for singly-linked list.
 **/
struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
};

class Solution1 { // iterative
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *start = nullptr, *nxt = nullptr;
        while (head) {
             nxt = head->next;
             head->next = start;
             start = head;
             head = nxt;
        }
        return start;
    }
};

class Solution { // recursive
public:
    ListNode* reverseList(ListNode* head) {
        return reverse_llst_helper(head, nullptr);
    }
private:
    ListNode* reverse_llst_helper(ListNode* head, ListNode* start) {
        if (!head)
            return start;
        else {
            ListNode* nxt = head->next;
            head->next = start;
            return reverse_llst_helper(nxt, head);
        }
    }
};

void printLinkedList(ListNode *head) {
     string llst = "";
     while (head) {
            cout << head->val;
            if (head->next) {
                cout << " -> ";
            };
            head = head->next;
     };
     cout << endl;
}

int main(void) {
    Solution s;
    struct ListNode test(1);
    struct ListNode t1(2);
    struct ListNode t2(3);
    struct ListNode t3(4);
    struct ListNode t4(5);
    (&test)->next = &t1;
    (&test)->next->next = &t2;
    (&test)->next->next->next = &t3;
    (&test)->next->next->next->next = &t4;
    printLinkedList(s.reverseList(&test));
    return 0;
};