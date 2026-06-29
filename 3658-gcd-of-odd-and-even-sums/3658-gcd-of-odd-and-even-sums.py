class Solution(object):
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    def gcdOfOddEvenSums(self, n):
        x = 0
        y = 0

        for i in range(1, n + 1):
            x+= 2 * i - 1
            y += 2 * i
        return self.gcd(x,y)

        