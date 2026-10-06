class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cont=[]
        for i in range(0,len(nums)):
            if nums[i] in cont:
                return True
            cont.append(nums[i])
        return False