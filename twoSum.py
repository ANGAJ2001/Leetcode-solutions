class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b = [0]
        for i in range(len(nums)):
            
            for j in range(1,len(nums)):
                if(i!=j and nums[i]+nums[j]== target):
                    a = [i,j]
                    return a
        return b
