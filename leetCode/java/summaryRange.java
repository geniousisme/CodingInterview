import java.util.ArrayList;
import java.util.List;
import util.func.Util;

public class summaryRange {
    public static void main(String[] args) {
        int[] test1 = {0, 1, 2, 4, 5, 7};
        Util.print_str_lst(summaryRanges(test1)); 
    }
    public static List<String> summaryRanges(int[] nums) {
        List<String> res = new ArrayList<String>();
        if (nums.length != 0) {
            String prev = String.valueOf(nums[0]);
            String post = null;
            for (int i = 1; i < nums.length; i++) {
            	if (nums[i] == nums[i - 1] + 1) {
            		post = "->" + String.valueOf(nums[i]);
            	} else {
            		post = prev + (post != null ? post : "");
            		res.add(post);
            		post = null;
            		prev = String.valueOf(nums[i]);
            	}
            }
            res.add(prev + (post != null ? post : ""));
        }
        return res;
    }
}