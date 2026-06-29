class Solution(object):
    def maxProfit(self, prices):
            minprice=prices[0]
            profit=0
            for i in range(1,len(prices)):
                curprofit=prices[i]-minprice
                if curprofit>profit:
                    profit=curprofit
                minprice=min(minprice,prices[i])
            return profit


        