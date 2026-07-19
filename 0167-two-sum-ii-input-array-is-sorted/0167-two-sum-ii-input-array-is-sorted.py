class Solution(object):
    def twoSum(self, numbers, target):
        sem={}
        for i in range(len(numbers)):
            rem=target-numbers[i]
            if rem in sem:
                return (sem[rem]+1,i+1)
            sem[numbers[i]]=i
        
        