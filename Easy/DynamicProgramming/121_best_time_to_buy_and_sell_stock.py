from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Minimum price seen so far (buying price)
        max_profit = 0  # Maximum profit so far

        for price in prices:
            if price < min_price:
                # Update the minimum price if a lower one is found
                min_price = price
            else:
                # Calculate profit if selling at the current price
                profit = price - min_price
                # Update max profit if this profit is higher
                if profit > max_profit:
                    max_profit = profit

        return max_profit