class Solution(object):
    def sortString(self,s):
        s1=list(s)
        s1.sort()
        return "".join(s1)
    def groupAnagrams(self, strs):
        fre={}
        for i in strs:
            key=self.sortString(i)
            if key in fre:
                fre[key].append(i)
            else:
                fre[key]=[i]
        return list(fre.values())

        
        