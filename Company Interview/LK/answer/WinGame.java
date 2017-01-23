
public class WinGame {
/*
 * 
 * 
 * boolean canIWin(int maxNum, int target)，
 * 从1,2...maxNum的数组里两个玩家轮流选数，
 * 第一个达到sum>=target的玩家获胜，问如何判断先选的玩家能获胜。
 * sum是指连个玩家一起选的数的和
 * 
 */
	
	public static boolean canWin(int maxNum, int target) {
		boolean[] isUsed = new boolean[maxNum + 1];
		return helper(isUsed, target, maxNum);
	}
	
	public static boolean helper(boolean[] isUsed, int target, int maxNum) {
		if (maxNum < 0) {
			return false;
		}
		boolean isEmpty = true;
		for (boolean used : isUsed) {
			if (!used) {
				isEmpty = false;
			}
		}
		if (isEmpty) {
			return false;
		}
		if (target <= 0) {
			return false;
		}
		boolean canWin = false;
		for (int i = 1; i <= maxNum; i++) {
			if (!isUsed[i] && i >= target) {
				return true;
			}
			if (!isUsed[i]) {
				isUsed[i] = true;
				canWin = canWin || !helper(isUsed, target - i, maxNum);
				isUsed[i] = false;
			}
		}
		return canWin;
	}
	
	public static boolean canIWin(int[] numberPool, int target) {
        boolean isEmpty = true;
        for (int data : numberPool)
            if (data > 0) isEmpty = false; 
        if (isEmpty) return false;
        else {
            if (target <= 0) return false;
            for (int data : numberPool)
                if (data > 0 && data >= target) return true;
            boolean canIWinFlag = false;
            for (int i = 0; i < numberPool.length && numberPool[i] > 0; ++i) {
                int data = numberPool[i];
                numberPool[i] = -1;
                canIWinFlag = canIWinFlag || !canIWin(numberPool, target - data); // other's turn
                numberPool[i] = data;
            }
            return canIWinFlag;
        }
    }
	
	public static void main(String[] args) {
		int[] a = {1, 2, 3, 4, 5, 6, 7};
		//System.out.print(canIWin(a, 17));
		System.out.print(canWin(6, 17));
	}
}
