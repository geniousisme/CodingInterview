public class Solution {
    public String addStrings(String num1, String num2) {
        int i1 = num1.length() - 1, i2 = num2.length() - 1, digit = 0, carry = 0;
        String res = "";

        while(i1 >= 0 || i2 >= 0) {
            digit = carry;

            if (i1 >= 0) {
                digit += num1.charAt(i1--) - '0';
            }

            if (i2 >= 0) {
                digit += num2.charAt(i2--) - '0';
            }
            res = Integer.toString(digit % 10) + res;
            carry = digit / 10;
        }

        if (carry > 0) {
            res = '1' + res;
        }

        return res;
    }
}