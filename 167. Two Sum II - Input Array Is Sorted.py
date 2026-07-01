class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<=j:
            su=numbers[i]+numbers[j]
            if su == target:
                return [i+1,j+1]
            elif su > target:
                j-=1
            else:
                i+=1
#-------------------------or-----------------------------------#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(numbers)):
            rem = target - numbers[i]
            if rem in d:
                return [d[rem]+1,i+1]
            d[numbers[i]]=i
