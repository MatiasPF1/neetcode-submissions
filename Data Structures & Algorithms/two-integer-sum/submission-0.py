class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = {}
        for index,value in enumerate(nums):
            searched =  target - value
            if searched in dicti:
                return [dicti[searched], index]
            else:
                dicti[value] = index
        return []
            

        