class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max=candies[0]
        x=[]
        for i in candies:
            if i>max:
                max=i
        for i in range(len(candies)):
            candies[i]+=extraCandies
            if candies[i]>=max:
                x.append(True)
            else:
                x.append(False)
        return x
        