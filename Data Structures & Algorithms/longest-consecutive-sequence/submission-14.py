class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Nums_set=set(nums)
        Answer=1

        if len(Nums_set) == 0:
            return 0 

        for i in nums:
            if i-1 not in Nums_set:
                temp = 1
                while i+1 in Nums_set:
                    temp +=1
                    Answer=max(Answer,temp)
                    i+=1
        return Answer
        

            

        



            
            
                


        
                


            
        