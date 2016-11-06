/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

import java.util.Random;

public class Solution {

    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    public Solution(ListNode head) {
        h = head;
        r = new Random();
    }
    
    /** Returns a random node's value. */
    public int getRandom() {
        int count = 1;
        int result = 0;
        ListNode node = h;
        while (node != null) {
        	if (r.nextInt(count) == 0) {
        		result = node.val;
        	}
        	count++;
        	node = node.next;
        }
        return result;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */