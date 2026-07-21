class Solution(object):
    def isAnagram(self, s, t):
        fre={}
        que={}
        if len(s) != len(t):
           return False
        for i in range(len(s)):
            if s[i] in fre:
                fre[s[i]] += 1
            else:
                fre[s[i]] = 1
        for j in range(len(t)):
            if t[j] in que:
                que[t[j]] += 1
            else:
                que[t[j]] = 1
        if fre==que:
            return True
        else:
            return False
            
        