class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        sign = '+'

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(float(stack.pop()) / num))

                sign = s[i]
                num = 0

        return sum(stack)