class Solution(object):
    def search(self, nums, target):
        low,high=0,len(nums)-1
        while low <= high:
            mid=(low+high)//2 #choose the middle index of nums
            if nums[mid]==target:
                return mid
            elif nums[mid] < target:
                low = mid +1#shift the low index to the mid 
            else:
                high = mid -1#shift the high index to the mid
        if target in nums:
            return mid
        else:
            return -1