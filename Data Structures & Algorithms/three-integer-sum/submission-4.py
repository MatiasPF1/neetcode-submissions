class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        responses=[]
        nums.sort() #need to sort to transform it into two sum array is sorted

        # static value logic 
        for index,value in enumerate(nums):
            if index> 0 and value == nums[index-1]:   #skip value if appeared to not re use it
                continue 
        #two pointers logic
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
                    left +=1     #whichever more work , just adapt the while lool
                    while nums[left] == nums[left -1] and left < right:
                        left  +=1
        return responses
                

            