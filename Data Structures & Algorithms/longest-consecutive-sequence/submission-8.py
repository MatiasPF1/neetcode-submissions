class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        listi=sorted(set(nums))
        dicti= {}
        counter = 0
        tmp = 1

        for i in listi:
            if i not in dicti:
                dicti[i] = 1
    
        for i in listi:
            if i-1 not in dicti: #first one
                tmp=1
                counter = max(counter,tmp)
            if i-1 in dicti:
                tmp +=1 
                counter = max(counter,tmp)
        return counter



            
            
                


        
                


            
        