public class majorityElementII {
    public List<Integer> majorityElement(int[] nums) {
        int candidate1 = 0;
        int candidate2 = 0;
        int cand1_count = 0;
        int cand2_count = 0;
        for (int num: nums) {
        	if (candidate1 == num) {
        		cand1_count += 1;
        	} else if (candidate2 == num) {
        		cand2_count += 1;
        	} else if (cand1_count == 0) {
        		candidate1 = num;
        		cand1_count = 1;
        	} else if (cand2_count == 0) {
        		candidate2 = num;
        		cand2_count = 1;
        	} else {
        		cand1_count -= 1;
        		cand2_count -= 1;
        	}
        }

        cand1_count = 0;
        cand2_count = 0;
        for (int num: nums) {
        	if (num == candidate1) {
        		cand1_count += 1;
        	}
        	if (num == candidate2) {
        		cand2_count += 1;
        	}
        }
        List<Integer> res = new ArrayList<Integer>();
        if (cand1_count > nums.length / 3) {
        	res.add(candidate1);
        }
        if (cand2_count > nums.length / 3) {
        	res.add(candidate2);
        }
        return res;
    }
}