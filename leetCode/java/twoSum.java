import java.util.HashMap;

public class twoSum {
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) != null) {
                int[] result = {map.get(nums[i]) + 1, i + 1};
                return result;
            }
            map.put(target - nums[i], i);
        }
        int[] result = {};
        return result;
    }
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = twoSum(nums, target);
        for (int idx: result) {
            System.out.println(idx);
        }
    }
}