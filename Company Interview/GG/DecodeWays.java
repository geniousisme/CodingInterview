import java.util.ArrayList;
import java.util.List;

// public class DecodeWays {
//     public static void main(String[] args) {
//         System.out.println(numDecodings("10"));
//     }
//     public static int numDecodings(String s) {
//         int len = s.length();
//         if (len == 0) {
//             return 0;
//         }
//         if (len == 1) {
//             System.out.println("Hey");
//             if (isValidForDecoding(s.substring(0, 1))) {
//                 return 1;
//             } 
//             else {
//                 return 0;
//             }
//         }
//         int res = 0;
//         if (isValidForDecoding(s.substring(len - 1, len))) {
//             System.out.println("1");
//             res += numDecodings(s.substring(0, len - 1));
//         }
//         if (isValidForDecoding(s.substring(len - 2, len))) {
//             System.out.println("2");
//             res += numDecodings(s.substring(0, len - 2));
//         }
//         return res;
//     }

//     private static boolean isValidForDecoding(String s) {
//         System.out.println("input s " + s);
//         if (s.length() == 0) {
//             return false;
//         }
//         int num = Integer.parseInt(s);
//         System.out.println("num: " + num);
//         if (num >= 1 && num <= 26) {
//             return true;
//         }
//         else {
//             return false;
//         }
//     }
// }

public class DecodeWays {
    private static int res_count = 0;

    public static void main(String[] args) {
        System.out.println(numDecodings("11"));
    }

    public static int numDecodings(String s) {
        return helper(s, 0);
    }
    
    public static int helper(String s, int index) {
        if(s == null || s.length() == 0)  return 0;
        if(index == s.length()) return 1;
        int onechar = 0, twochars = 0;
        int count = 0;
      
        if(index + 1 <= s.length()) onechar = Integer.valueOf(s.substring(index, index + 1));
        if(index + 2 <= s.length()) twochars = Integer.valueOf(s.substring(index, index + 2));
        if(onechar >= 1 && onechar <= 9) {
            count += helper(s, index + 1);
        }
        if(twochars >= 10 && twochars <= 26) {
            count += helper(s, index + 2);
        }
        
        return count;
    }
}
/*
* Time: O(N)
* Space: O(N)
*/
// public class Solution2 {
//     public int numDecodings(String s) {
//         if (s.length() == 0 || s == null || s.charAt(0) == '0') {
//             return 0;
//         }
//         List<Integer> dp = new ArrayList<Integer>();
//         dp.add(1);
//         dp.add(1);
//         for (int i = 2; i < s.length() + 1; i++) {
//             String sub_int_str = s.substring(i - 2, i);
//             int sub_int = Integer.parseInt(sub_int_str);
//             if (sub_int >= 10 && sub_int <= 26) {
//                 if (sub_int_str.charAt(1) != '0') {
//                     dp.add(dp.get(i - 1) + dp.get(i - 2));
//                 }
//                 else {
//                     dp.add(dp.get(i - 2));
//                 }
//             }
//             else if (s.charAt(i - 1) != '0') {
//                 dp.add(dp.get(i - 1));
//             }
//             else {
//                 return 0;
//             }
//         }
//         return dp.get(s.length());
//     }
// }


// /*
// * Time: O(N)
// * Space: O(1)
// */

// public class Solution3 {
//     public int numDecodings(String s) {
//         if (s.length() == 0 || s == null || s.charAt(0) == '0') {
//             return 0;
//         }
//         int prev = 1;
//         int prev_prev = 0;
//         for (int i = 0; i < s.length(); i++) {
//             int curr = 0;
//             if (s.charAt(i) != '0') {
//                 curr = prev;
//             }
//             if (i > 0 && (s.charAt(i - 1) == '1' || (s.charAt(i - 1) == '2' && s.charAt(i) <= '6'))) {
//                 curr += prev_prev;
//             }
//             prev_prev = prev;
//             prev = curr;
//         }
//         return prev;
//     }
// }