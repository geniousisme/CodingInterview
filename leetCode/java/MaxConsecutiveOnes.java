public class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int one_count = 0;
        int max_one_count = 0;

        for (int num: nums) {
            if (num == 0) {
                one_count = 0;
            } else {
                one_count++;
                max_one_count = Math.max(max_one_count, one_count);
            }
        }

        return max_one_count;
    }
}