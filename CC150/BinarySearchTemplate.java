public class BinarySearchTemplate {
  public static void main(String[] args) {
    int[] nums = {1, 2, 4, 5, 7, 9, 10};
    System.out.println("\nIterative:");
    System.out.println(binarySearchIterative(nums, 4));
    System.out.println(binarySearchIterative(nums, 1));
    System.out.println(binarySearchIterative(nums, 10));
    System.out.println(binarySearchIterative(nums, 11));
    System.out.println(binarySearchIterative(nums, 0));

    System.out.println("\nRecursive:");
    System.out.println(binarySearchRecursive(nums, 4));
    System.out.println(binarySearchRecursive(nums, 1));
    System.out.println(binarySearchRecursive(nums, 10));
    System.out.println(binarySearchRecursive(nums, 11));
    System.out.println(binarySearchRecursive(nums, 0));
  }

  public static int binarySearchIterative(int[] nums, int target) {
    if (nums.length == 0 || nums == null) {
      return -1;
    }
    int start = 0, end = nums.length - 1;
    while (start + 1 < end) {
      int mid = start + (end - start) / 2;
      if (nums[mid] == target) {
          return mid;
      } else if (nums[mid] < target) {
          start = mid;
      } else {
          end = mid;
      }
    }
    if (nums[start] == target) {
      return start;
    }
    if (nums[end] == target) {
      return end;
    }
    return -1;
  }

  public static int binarySearchRecursive(int[] nums, int target) {
    if (nums.length == 0 || nums == null) {
      return -1;
    }
    return binarySearchRecursiveHelper(nums, target, 0, nums.length - 1);
  }

  public static int binarySearchRecursiveHelper(int[] nums, int target, int start, int end) {
    if (start + 1 >= end) {
      if (nums[start] == target) {
        return start;
      }
      if (nums[end] == target) {
        return end;
      }
      return -1;
    }
  
    int mid = start + (end - start) / 2;

    if (nums[mid] > target) {
      return binarySearchRecursiveHelper(nums, target, start, mid);
    }
    if (nums[mid] < target) {
      return binarySearchRecursiveHelper(nums, target, mid, end);
    }
    return mid;
  }
}
