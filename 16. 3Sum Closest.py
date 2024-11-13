class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest=float('inf')#compare with large value
        nums.sort()
        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if abs(total-target)<abs(closest-target):#choose the closest value
                    closest=total
                if total==target:#if it is the exact value 
                    return total
                if total<target:
                    left+=1
                if total>target:
                    right-=1
        return closest

        