public class Solution {
    public static void main(String[] args) {

    }
    public static boolean isUgly(int num) {
        if (num < 1) {
        	return false;
        }
        while (num > 1) {
        	if (num % 2 == 0) {
        		num /= 2;
        		continue;
        	}
        	else if (num % 3 == 0) {
        		num /= 3;
        		continue;
        	}
        	else if (num % 5 == 0) {
        		num /= 5;
        		continue;
        	}
        	else {
        		return false;
        	}
        }
        return true;
    }
}