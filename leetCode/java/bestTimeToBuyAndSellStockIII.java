import java.lang.Math;

public class bestTimeToBuyAndSellStockIII {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) {
            return 0;
        }
        int[] left = new int[prices.length];
        int[] right = new int[prices.length];
        left[0] = 0;
        right[right.length - 1] = 0;

        int minV = prices[0];
        int maxV = prices[prices.length - 1];

        for (int i = 1; i < left.length; i++) {
            minV = Math.min(prices[i], minV);
            left[i] = Math.max(left[i - 1], prices[i] - minV);
        }

        for (int j = right.length - 2; j > -1; j--) {
            maxV = Math.max(prices[j], maxV);
            right[j] = Math.max(right[j + 1], maxV - prices[j]);
        }

        int max_diff = 0;
        for (int k = 0; k < prices.length; k++) {
            if (left[k] + right[k] > max_diff) {
                max_diff = left[k] + right[k];
            }
        }

        return max_diff;
    }
}