class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            count=nums[i]
            for j in range(i):
                count=nums[j]+count
            ans.append(count)
        return ans
