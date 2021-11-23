class Solution(object):
    def twoSum(self,nums, target):
        for i in nums:
            for j in nums:
                if i==j:
                    continue
                if i+j == target:
                    return [i,j]
        return []
    def twosumbet(self, nums, target):
        hash={}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hash:
                return [hash[diff],n]
            hash[n]=i
        return []

print(Solution().twosumbet([2,7,11,15],17))
print(Solution().twoSum([2,7,11,15],17))