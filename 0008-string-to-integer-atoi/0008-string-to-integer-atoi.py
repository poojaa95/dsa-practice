class Solution(object):
    def myAtoi(self, s):
        ans = ""
        sign = 1
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        for j in range(i,len(s)):
            if s[j].isdigit():
                ans+=s[j]
            else:
                break
        if ans=="":
            return 0
        x = sign * int(ans)

        # overflow fix
        if x < -2**31:
            return -2**31
        if x > 2**31 - 1:
            return 2**31 - 1

        return x
       
        