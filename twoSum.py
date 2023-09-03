class Solution:
    # Time Complexity : O(N)
    # Space Complexity : O(N)
    # Create a hashMap and update it with value as key and index as value
    def twoSum( nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
    
     # Test cases
    print(twoSum([2,7,11,15],9))