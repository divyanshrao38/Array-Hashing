class Solution:
    # time complexity: O(N)
    # Space Complexity: O(N)
    # Take a hashmap and update freq of s and then check for t
    def isAnagram( s: str, t: str) -> bool:
        freq = {}
        for i in s:
            if i not in freq.keys():
                freq[i] = 0
            freq[i] +=1

        for i in t:
            if i not in freq.keys():
                return False
            freq[i] -= 1
            if freq[i] <0:
                return False
        for key, value in freq.items():
            if value > 0:
                return False
        return True
    
    # Test cases
    print(isAnagram('anagram',"nagaram"))