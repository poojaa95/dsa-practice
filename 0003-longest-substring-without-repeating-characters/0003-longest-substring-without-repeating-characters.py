class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res=0
        for i in range(len(s)):
            ans=""
            for j in range(i,len(s)):
               if s[j] not in ans:
                   ans+=s[j]
                   res=max(res,len(ans))
               else:
                    break
        return res
        