class Solution(object):
    def twoSum(self, nums, target):
       for i in range(len(nums)):
           for j in range(i+1,len(nums)): # use nested for loop to test each couples of numbers 
               if (i!=j and nums[i]+nums[j]==target): # check whether the summation is equal to target or not
                 return [i,j]
             
