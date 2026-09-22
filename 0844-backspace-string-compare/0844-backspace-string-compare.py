class Solution(object):
    def backspaceCompare(self, s, t):
#         slow,fast=0,0
#         while slow<len(s) and fast<len(t):
#             if s[slow]!='#' and t[fast]!='#':
#                 slow+=1
#                 fast+=1
#             s[slow+1]=s[slow-1]
#             t[fast+1]=t[fast-1]
#         if s==t:
#             return True
#         else:
#             return False
        a=[]
        b=[]
        for i in s:
            if i!='#':
                a.append(i)
            elif a:
                a.pop()
        for i in t:
            if i!='#':
                b.append(i)
            elif b:
                b.pop()
        if a==b:
            return True
        else:
            return False
            