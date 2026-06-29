class Solution(object):
    def isValid(self, s):
        l = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                l.append(ch)

            elif ch == ')':
                if len(l) == 0 or l[-1] != '(':
                    return False
                l.pop()

            elif ch == ']':
                if len(l) == 0 or l[-1] != '[':
                    return False
                l.pop()

            elif ch == '}':
                if len(l) == 0 or l[-1] != '{':
                    return False
                l.pop()

        return len(l) == 0