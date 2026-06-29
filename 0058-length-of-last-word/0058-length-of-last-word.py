class Solution(object):
    def lengthOfLastWord(self, s):
        # ans=""
        # for i in range(len(s)-1,-1,-1):
        #     if s[i]!=" ":
        #         ans+=s[i]
        #     else:
        #         break
        # return len(ans)
        
        ans=""
        i=len(s)-1
        while i>=0 and s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            ans+=s[i]
            i-=1
        return len(ans)
        