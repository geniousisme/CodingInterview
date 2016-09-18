public class majorityElement {
    public static void main(String[] args) {
    	int[] test1 = {1, 1, 2};
    	System.out.println(majorityElement(test1));
    	int[] test2 = {1, 2, 2};
    	System.out.println(majorityElement(test2));
    	int[] test3 = {1, 2, 2, 1, 2, 3, 3, 2};
    	System.out.println(majorityElement(test2));
    }

    public static int majorityElement(int[] nums) {
    	int candidate = 0;
    	int cand_count = 0;
    	for (int num: nums) {
    		if (cand_count == 0) {
    			candidate = num;
    			cand_count = 1;
    		} else {
	    		if (candidate == num) {
	    			cand_count += 1;
	    		} else {
	    			cand_count -= 1;
	    		}
    		}
    	}
    	return candidate;
    }
}