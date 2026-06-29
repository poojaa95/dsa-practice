class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        tot=0
        for i in range(len(cost)):
            if i%3!=2:
                tot+=cost[i]
        return tot
        