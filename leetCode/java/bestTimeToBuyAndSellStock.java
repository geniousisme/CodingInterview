public class bestTimeToBuyAndSellStock {
	public static void main(String[] args) {
		int[] prices = {7, 1, 5, 3, 6, 4};
		System.out.println(maxProfit(prices));
	}

    public static int maxProfit(int[] prices) {
    	int min_price = Integer.MAX_VALUE;
    	int max_price_diff = 0;
        for (int price: prices) {
        	if (min_price > price) {
        		min_price = price;
        	}
        	if (price - min_price > max_price_diff) {
        		max_price_diff = price - min_price;
        	}
        }
        return max_price_diff;
    }
}