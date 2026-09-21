class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # k=[]
        # k.extend(nums1[:m])
        # k.extend(nums2[:n])   
        # k.sort()
        # for i in range(m+n):
        #     nums1[i]=k[i]
        # return k    

        # lef1,lef2=0,0
        # pos=0
        # nums3=[0]* (m+n)
        # while lef1<m and lef2<n:
        #     if nums1[lef1]>nums2[lef2]:
        #         nums3[pos]=nums2[lef2]
        #         lef2+=1
        #     else:
        #         nums3[pos]=nums1[lef1]
        #         lef1+=1
        #     pos+=1
        # while lef1<m:
        #     nums3[pos]=nums1[lef1]
        #     pos+=1
        #     lef1+=1
        # while lef2<n:
        #     nums3[pos]=nums2[lef2]
        #     pos+=1
        #     lef2+=1
        # for i in range(m+n):
        #     nums1[i]=nums3[i]
        # return nums1

        lef1=m-1
        lef2=n-1
        pos=m+n-1
        while lef1>=0 and lef2>=0:
            if nums1[lef1] > nums2[lef2]:
                nums1[pos]=nums1[lef1]
                lef1-=1
                pos-=1
            else:
                nums1[pos]=nums2[lef2]
                lef2-=1
                pos-=1
        while lef2>=0:
            nums1[pos]=nums2[lef2]
            lef2-=1
            pos-=1

