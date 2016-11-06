
public class pickSmallest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(pick(233614));
		System.out.println(pick(1578));
		System.out.println(pick(135));
		System.out.println(pick(1000000000));
	}
	
	public static int pick(int num) {
		String rst = null;
		String temp = String.valueOf(num);
		for(int i = temp.length()-1; i>0 ; i--){
			if(temp.charAt(i) > temp.charAt(i-1)) {
				if(i== temp.length()-1) {
					rst = temp.substring(0, i-1)+temp.charAt(i);
				} else {
					rst = temp.substring(0, i)+temp.charAt(i)+temp.substring(i+2,temp.length());
				} 
				break;
			}
		}
		if (rst == null) {
            rst = temp.charAt(0) + temp.substring(2, temp.length());
        }
		return (int)Integer.valueOf(rst);
	}

}


import java.util.Stack;
import java.util.regex.Pattern;

public class fileDistance {

	private final static String s = "a";
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String input = "dir1\n dir11\n dir12\n  picture.jpeg\n  dir121\n  file.txt\ndir2\n file2.gif";
		System.out.println("rst -- "+sumPath(input));
	
	}
	
	public static boolean isImage(String s){
		String patterns = "([^\\s]+(\\.(?i)(jpg|png|gif|bmp|jpeg))$)";
		Pattern pattern = Pattern.compile(patterns);
		return pattern.matcher(s).matches();
	}

	public static int sumPath(String s) {
		String[] lines = s.split("\n");
		int curLayer = 0;
		int curLength = 0;
		int rst = 0;
		Stack<String> stack =  new Stack<>();
		for(String temp : lines) {
			System.out.println(temp);
			int tempLayer = temp.indexOf(temp.trim());
			if(tempLayer <= curLayer) {
				while(!stack.isEmpty() && (tempLayer <= curLayer)){
					String last = stack.pop();
					curLength = curLength - last.length();
					curLayer--;
				}
			}	
			curLayer = tempLayer;
			String cur = temp.trim();
			stack.push("/"+cur);
			curLength = curLength + stack.peek().length();
			if(isImage(cur)) {
				System.out.println("current path length -- "+curLength);
				rst = rst + curLength;
			}
		}
		return rst;
		
	}

}
