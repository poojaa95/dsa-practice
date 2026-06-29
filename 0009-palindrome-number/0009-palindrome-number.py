class Solution(object):
    def isPalindrome(self, x):
      rem=0
      rev=0
      n=abs(x)
      while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
      if rev==x:
        return True
      else:
        return False


        