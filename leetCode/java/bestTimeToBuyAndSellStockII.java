public class bestTimeToBuyAndSellStockII {
    public int maxProfit(int[] prices) {
    	int diff_sum = 0;
    	for (int i = 1; i < prices.length; i++) {
    		int diff = prices[i] - prices[i - 1];
    		if (diff > 0) {
    			diff_sum += diff;
    		}
    	}
    	return diff_sum;
    }
}