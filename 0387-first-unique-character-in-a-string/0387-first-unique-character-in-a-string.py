class Solution(object):
    def firstUniqChar(self, s):
        uni={}
        for i in s:
            if i not in uni:
                uni[i]=1
            else:
                uni[i]+=1
        for i in range(len(s)):
            if uni[s[i]]==1:
                return i
        return -1

            
                
        print(uni)
        