class Solution(object):
    def removeDuplicates(self, nums):
        # l=[]
        # for i in range(len(nums)):
        #     l.append(nums[i])
        #     if l.count(l[-1])>2:
        #        l.remove(l[-1])

        # for i in range(len(l)):
        #     nums[i]=l[i]
        # return len(l)
        n=len(nums)
        if n<=2:
            return n
        k=2
        for i in range(2,n):
            if nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k+=1
        return k