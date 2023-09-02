import collections
class Solution:
    # Time and Space Complexity: O(NK)
    # Take a dict and store either the count or sorted strings and return the values
    def groupAnagramsCount( strs: list[str]) -> list[list[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
    
    def groupAnagramsSorted( strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    print(groupAnagramsCount(["eat","tea","tan","ate","nat","bat"]))