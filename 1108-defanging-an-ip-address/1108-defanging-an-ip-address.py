class Solution(object):
    def defangIPaddr(self, address):
        # return address.replace(".","[.]")
        ans=""
        for i in address:
            if i!='.':
                ans+=i
            else:
                i='[.]'
                ans+=i
        return ans