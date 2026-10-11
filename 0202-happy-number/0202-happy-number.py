class Solution(object):
    def isHappy(self, n):
        rem=0
        while n!=1 and n!=4:
            sume=0
            while n>0:
                rem=n%10
                sume+=rem*rem
                n=n//10
            n=sume
        if n==1:
            return True
        else:
            return False
        