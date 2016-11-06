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
			System.out.println(temp.trim());
			int tempLayer = temp.indexOf(temp.trim());
			System.out.println("tempLayer: " + tempLayer);
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
