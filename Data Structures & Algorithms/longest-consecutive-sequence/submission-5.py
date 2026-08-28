class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        listi_NoRepeat=set(nums)
        dicti={}
        counter=0
        Longest=0
        for i in nums:
            dicti[i]=0
        
        for i in listi_NoRepeat:
            if i-1 not in dicti:                #is this the first in the consecutive sequence ?
                counter = 1                     #count itself & reseter for each string
                while i+1 in dicti:             #go 1 by 1 
                    counter+=1
                    i +=1
                Longest= max(Longest,counter)
        return Longest

                

       


        