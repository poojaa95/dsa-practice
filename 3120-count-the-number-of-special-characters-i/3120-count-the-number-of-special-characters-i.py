class Solution(object):
    def numberOfSpecialChars(self, word):
        spec=0
        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in word and ch.upper() in word:
                    spec+=1
        return spec