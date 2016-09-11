public class pickSmallest {
	public static void main(String[] args) {
		System.out.println(pick_smallest(233614));
		System.out.println(pick_smallest(1578));
		System.out.println(pick_smallest(135));
		System.out.println(pick_smallest(10000));
	}

	public static int pick_smallest(int num) {
		int smallest_num = Integer.MAX_VALUE;
		String num_string = String.valueOf(num);
		for (int i = 0; i < num_string.length() - 1; i++) {
			char replace_int_str = num_string.charAt(i) > num_string.charAt(i + 1) ? num_string.charAt(i) : num_string.charAt(i + 1);
			int temp = (int)Integer.valueOf(num_string.substring(0, i) 
					+ replace_int_str + num_string.substring(i + 2, num_string.length()));
			if (temp < smallest_num) {
				smallest_num = temp;
			}
		}
		return smallest_num;
	}

}