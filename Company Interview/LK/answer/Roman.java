import java.util.HashMap;


public class Roman {
	public static int romanToInteger(String s) throws Exception {
		if (s.length() == 0 || s == null) {
		        return 0;
		}
		HashMap<Character, Integer> dict = new HashMap<Character, Integer>();
		dict.put('I', 1);
		dict.put('V', 5);
		dict.put('X', 10);
		dict.put('L', 50);
		dict.put('C', 100);
		dict.put('D', 500);
		dict.put('M', 1000);
		int len = s.length();
		int result = dict.get(s.charAt(len - 1));
		// check illegal input
		int sameCount = 1;
		for (int i = 0; i < len; i++) {
			if (!dict.containsKey(s.charAt(i))) {
				throw new Exception("Illegal input: invalid character " + s.charAt(i));
			}
			if (i < len - 1 && dict.get(s.charAt(i)) < dict.get(s.charAt(i + 1))) {
				int diff = dict.get(s.charAt(i + 1)) - dict.get(s.charAt(i));
				if (diff != 4 && diff != 9 && diff != 40 && diff != 90 && diff != 400 && diff != 900) {
					throw new Exception("Illegal input: invalid sequence " + s.charAt(i) + s.charAt(i + 1));
				}
			}
			if (i > 0 && s.charAt(i) == s.charAt(i - 1)) {
				sameCount++;
			} else {
				sameCount = 1;
			}
			if (sameCount > 1) {
				if (s.charAt(i) == 'V' || s.charAt(i) == 'L' || s.charAt(i) == 'D') {
					throw new Exception("Illegal input: 2 or more consecutive " + s.charAt(i));
				}
			}
			if (sameCount > 3) {
				throw new Exception("Illegal input: 4 or more consecutive " + s.charAt(i));
			}
		}
		
		for (int i = 0; i < len - 1; i++) {
		    if (dict.get(s.charAt(i)) >= dict.get(s.charAt(i + 1))) {
		        result += dict.get(s.charAt(i));
		    } else {
		        result -= dict.get(s.charAt(i));
		    }
		}
		return result;
	}
	
	public static String integerToRoman(int num) {
		String[] sdict = {"M", "CM", "D", "CD", 
                "C", "XC", "L", "XL", "X", 
                "IX", "V", "IV", "I"};
		int[] idict = {1000, 900, 500, 400, 100,
              90, 50, 40, 10, 9, 5, 4, 1};
		String result = "";
		while (num > 0) {
		  int i;
		  for (i = 0; i < idict.length; i++) {
		      if (num >= idict[i]) {
		          result = result + sdict[i];
		          break;
		      }
		  }
		  num -= idict[i];
		}
		return result;
	}
	
	public static void main(String[] args) throws Exception {
		System.out.println(romanToInteger("XCV"));
		System.out.print(integerToRoman(95));
	}
	
}
