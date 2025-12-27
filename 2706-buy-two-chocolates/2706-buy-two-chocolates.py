class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        if len(prices)<2:
            return money
        prices.sort()
        i = 0
        s = prices[0] + prices[1]
        if (money-s)>=0:
            return money-s 
        return money 