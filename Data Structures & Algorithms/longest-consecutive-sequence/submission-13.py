class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Nums_set=set(nums)    
        answer=1                        

        if len(Nums_set) == 0:
            return 0


        # [2,3,4,5 10,20]
        for i in Nums_set:
            if i-1 not in Nums_set:
                temp = 1 
                while i+1 in Nums_set:
                    temp+=1
                    i+=1
                answer= max(temp,answer)
        return answer

            

        



            
            
                


        
                


            
        