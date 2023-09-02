class Solution:
    # Time Complexity : O(N)
    # Space Complexity : O(N)
    # Create a hashMao and update freq
    def containsDuplicate( nums: list[int]) -> bool:
        freq = {}
        for i in nums:
            if i not in freq.keys():
                freq[i] = 0
            freq[i] +=1

        for i in freq.keys():
            if freq[i] >= 2:
                return True

        return False
    
    # Test cases
    print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))