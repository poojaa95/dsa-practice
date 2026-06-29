class Solution(object):
    def reversePrefix(self, s, k):
       s=list(s)
       i=0
       j=k-1
       tem=s[i]
       while i<j:
           tem=s[i]
           s[i]=s[j]
           s[j]=tem
           i+=1
           j-=1
       return "".join(s)

         
        