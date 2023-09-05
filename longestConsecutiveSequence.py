class Solution:
    # time complexity: O(N)
#     Although the time complexity appears to be quadratic due to the while
# loop nested within the for loop, closer inspection reveals it to be
# linear. Because the while loop is reached only when currentNum marks
# the beginning of a sequence (i.e. currentNum-1 is not present in
# nums), the while loop can only run for nnn iterations throughout the
# entire runtime of the algorithm. This means that despite looking like
# O(n⋅n)O(n \cdot n)O(n⋅n) complexity, the nested loops actually run in O(n+n)=O(n)O(n + n) = O(n)O(n+n)=O(n)
# time. All other computations occur in constant time, so the overall
# runtime is linear.
# Space Complexity: O(N)
#  Take a num set and check if the previous number not in list then keep incrementing the streak
    def longestConsecutive( nums: list[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num +=1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak 
    print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))