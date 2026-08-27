class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dicti = {}
        
        #1-)Count how many times each number appears
        for num in nums:
            if num in Dicti:
                Dicti[num] += 1
            else:
                Dicti[num] = 1

        #2-) Creates a list of buckets([ [],[],[],[].....])
        freq = []
        for i in range(len(nums) + 1):
            freq.append([])


        #4-)Put each number in its frequency bucket
        for num in Dicti:
            frequency = Dicti[num]
            freq[frequency].append(num)
        result = []
        i = len(freq) - 1         # Start from highest frequency
        

        while i >= 0:
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

            i -= 1








        