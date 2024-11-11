class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[]
        nums.sort()
        for i in range(len(nums)-2):
            #skip duplicate elements
            if i > 0 and nums[i]==nums[i-1]:
                continue
            left,right=i+1,len(nums)-1#choose one element after i and another from the end
            while left<right:#until left and right have not reach each other
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    output.append([nums[i],nums[left],nums[right]])#consider all solutions
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return output
