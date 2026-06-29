class Solution(object):
    def maximumWealth(self, accounts):
        l=[]
        for i in range(len(accounts)):
            l.append(sum(accounts[i]))
        x=max(l)
        return x

        
        