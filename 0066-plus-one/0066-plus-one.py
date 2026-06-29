class Solution(object):
    def plusOne(self, digits):
       n=len(digits)
       num=0
       for i in range(n):
        num=num*10+digits[i]
       num+=1
       return [int(x) for x in str(num)]
        