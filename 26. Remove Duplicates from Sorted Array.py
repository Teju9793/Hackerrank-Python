class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set(nums)
        ls=len(s)
        x=len(nums)-len(s)
        nums[:]=sorted(list(s))+[0]*x
        return ls
