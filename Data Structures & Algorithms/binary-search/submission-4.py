class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums) -1
        middle = right - left // 2 

       
        if nums[middle] == target:
                return middle

        while middle >= left and middle <= right:
            if nums[middle] < target:
                if nums[right] == target: 
                    return right 
                else:
                    right -=1
            elif nums[middle] > target:
                if nums[left] == target:
                    return left
                else:
                    left +=1         
        return -1    
                

           
        

            

            
        