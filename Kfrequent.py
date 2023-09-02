from collections import Counter
import heapq
class Solution:
    # time complexity: O(Nlog⁡k)
    # Space complexity : O(N+k)
    def topKFrequent( nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k,count.keys(), key = count.get)
    # Approach 2: Quickselect (Hoare's selection algorithm)
    # Approach 3 : without built in function
    def topKFrequentVanilla( nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums
        count = {}
        freq = [ [] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for num, count in count.items():
            freq[count].append(num)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)== k:
                    return res
       
    
    print(topKFrequent([1,1,1,2,2,3,3],2))
    print(topKFrequentVanilla([1,1,1,2,2,3],2))