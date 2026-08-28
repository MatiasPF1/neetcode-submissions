class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        responses=[]
        nums.sort() #need to sort to transform it into two sum array is sorted

        for index,value in enumerate(nums):
            if index> 0 and value == nums[index-1]:   #skip  value to not re use it
                continue 
            left = index + 1
            right = len(nums) -1

            while left < right:
                summ = value + nums[left] + nums[right]
                if summ > 0:
                    right -=1
                if summ < 0:
                    left +=1
                if summ==0:
                    responses.append([value,nums[left],nums[right]])
                    left +=1
                    while nums[left] == nums[left -1] and left < right:
                        left  +=1
        return responses
                

            