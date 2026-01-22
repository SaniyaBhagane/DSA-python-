# Max Sum Subarray of size K
# https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
# Approach: Check every possible subarray of size k, calculate its sum, and keep updating the maximum sum found. Since we recompute the sum for each window from scratch, this approach is simple but not optimal.
# Complexity Analysis: Time=>0(n*n) space=> O(1)
# class Solution:
#     def maxSubarraySum(self, arr, k):
#         n = len(arr)
#         maxSum = float('-inf')
#         for i in range(0, n - k + 1):
#             currSum = 0
#             for j in range(i, i + k):
#                 currSum += arr[j]
#             maxSum = max(maxSum, currSum)
#         return maxSum
# Example Walkthrough
# Input:
# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# Step 1: First subarray (index 0 → 2)
# [2, 1, 5] → sum = 8
# maxSum = 8
# Step 2: Second subarray (index 1 → 3)
# [1, 5, 1] → sum = 7
# maxSum = 8
# Step 3: Third subarray (index 2 → 4)
# [5, 1, 3] → sum = 9
# maxSum = 9
# Step 4: Fourth subarray (index 3 → 5)
# [1, 3, 2] → sum = 6
# maxSum = 9
# Final Answer => Maximum subarray sum of size 3 = 9

# Approach 2: First calculate the sum of the first k elements. Then slide the window one step at a time by adding the new element entering the window and removing the element leaving it. Keep updating the maximum sum during this process
# Complexity Analysis: Time=>0(n) space=> O(1)
# class Solution:
#     def maxSubarraySum(self, arr, k):
#         n = len(arr)
#         # Step 1: sum of first window
#         windowSum = sum(arr[:k])
#         maxSum = windowSum
#         # Step 2: slide the window
#         for i in range(k, n):
#             windowSum += arr[i]        # add new element
#             windowSum -= arr[i - k]    # remove old element
#             maxSum = max(maxSum, windowSum)
#         return maxSum
# Example Walkthrough
# Input: arr = [2, 1, 5, 1, 3, 2]   k = 3
# Step 1: First window
# [2, 1, 5] → sum = 8
# max_sum = 8
# Step 2: Slide window
# Remove 2, add 1 → [1, 5, 1] → sum = 7
# Remove 1, add 3 → [5, 1, 3] → sum = 9  ← max
# Remove 5, add 2 → [1, 3, 2] → sum = 6
# Answer = 9

# ---------------------------------------------------------------------------------------
# 2461. Maximum Sum of Distinct Subarrays of Length K
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
# Approach: Generate all subarrays of length k, check if all elements are distinct using a list, and if yes, calculate the sum. Track the maximum valid sum. This is slow because we re-check uniqueness every time.
# Complexity Analysis: Time=>0(n*n) space=> O(1)
# class Solution:
#     def maximumSubarraySum(self, nums, k):
#         n = len(nums)
#         maxSum = 0
#         for i in range(n - k + 1):
#             temp = []
#             currSum = 0
#             valid = True
#             for j in range(i, i+k):
#                 if nums[j] in temp:
#                     valid = False
#                     break
#                 temp.append(nums[j])
#                 currSum += nums[j]
#             if valid:
#                 maxSum = max(maxSum, currSum)
#         return maxSum
# Example Walkthrough=> nums = [1,5,4,2,9,9,9], k = 3
# [1,5,4] → distinct ✅ sum = 10
# [5,4,2] → distinct ✅ sum = 11
# [4,2,9] → distinct ✅ sum = 15 ← max
# [2,9,9] → duplicate ❌
# [9,9,9] → duplicate ❌
# Answer = 15

# Approach 2: Use a sliding window of size k and a frequency map to track counts of elements. If any element’s count becomes greater than 1, shrink the window from the left. When the window size is exactly k and all elements are unique, update the max sum.
# Complexity Analysis: Time=>0(n) space=> O(n)
# class Solution:
#     def maximumSubarraySum(self, nums, k):
#         freq = {}
#         left = 0
#         currSum = 0
#         maxSum = 0
#         for right in range(len(nums)):
#             freq[nums[right]] = freq.get(nums[right], 0) + 1
#             currSum += nums[right]
#             # If duplicate appears, shrink window
#             while freq[nums[right]]> 1:
#                 freq[nums[left]] -= 1
#                 currSum -= nums[left]
#                 if freq[nums[left]] == 0:
#                     del freq[nums[left]]
#                 left += 1
#             # Window size exactly k
#             if right - left + 1 == k:
#                 maxSum = max(maxSum, currSum)
#                 # Slide window forward
#                 freq[nums[left]] -= 1
#                 currSum -= nums[left]
#                 if freq[nums[left]] == 0:
#                     del freq[nums[left]]
#                 left += 1
#         return maxSum
# Example Walkthrough => nums = [1,5,4,2,9,9,9], k = 3
# [1,5,4] → freq valid → sum = 10
# [5,4,2] → sum = 11
# [4,2,9] → sum = 15 ✅
# Duplicate 9 → shrink until unique again
# Final Answer = 15  

# -----------------------------------------------------------------------------------------------------
# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
# Approach: Check every possible subarray, calculate its sum, and track the smallest length whose sum ≥ target. This works but repeats sum calculations unnecessarily, making it inefficient for large inputs.
# Complexity Analysis: Time=>0(n*n) space=> O(1)
# class Solution:
#     def minSubArrayLen(self, target: int, nums: list[int]) -> int:
#         n = len(nums)
#         min_len = float('inf')
#         for i in range(n):
#             curr_sum = 0
#             for j in range(i, n):
#                 curr_sum += nums[j]
#                 if curr_sum >= target:
#                     min_len = min(min_len, j - i + 1)
#                     break
#         return 0 if min_len == float('inf') else min_len

# Approach 2: Use two pointers to maintain a sliding window.Expand the window to increase the sum and shrink it when the sum ≥ target to minimize the window size efficiently.
# Complexity Analysis: Time=>0(n) space=> O(1)
# class Solution:
#     def minSubArrayLen(self, target: int, nums: list[int]) -> int:
#         left = 0
#         curr_sum = 0
#         min_len = float('inf')
#         for right in range(len(nums)):
#             curr_sum += nums[right]
#             while curr_sum >= target:
#                 min_len = min(min_len, right - left + 1)
#                 curr_sum -= nums[left]
#                 left += 1
#         return 0 if min_len == float('inf') else min_len
# Example Walkthrough
# Input: target = 7   nums = [2,3,1,2,4,3]
# Sliding Window Steps:
# Expand → sum = 8 → window [2,3,1,2]
# Shrink from left → try smaller windows
# Best window found → [4,3]
# Output: 2

# ------------------------------------------------------------------------------------------------------
# 219. Contains Duplicates II:
# https://leetcode.com/problems/contains-duplicate-ii/description/
# Approach: For each index i, we look ahead up to k positions and check whether the same number appears again within this range. A set is used to track elements in the current window so duplicates can be detected quickly. If any duplicate is found within distance k, we return True; otherwise, after all checks, return False.
# Complexity Analysis: Time Complexity: O(n × k) Space Complexity: O(k) 
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i, min(i+k-1), n):
                if nums[j] in seen:
                    return True
                seen.add(nums[j])
        return False
# Example Walkthrough
# Input: nums = [1, 2, 3, 1], k = 3
# i = 0, window indices 0 → 3
# seen = {}
# j = 0 → add 1 → {1}
# j = 1 → add 2 → {1,2}
# j = 2 → add 3 → {1,2,3}
# j = 3 → 1 already in set → duplicate found → return True
# So the function stops early and returns True.

# Approach 2: We maintain a sliding window of at most k elements using a set. As we move forward, we remove the element that goes out of the window and check if the current element already exists in the set. If it does, a duplicate within distance k is found.
# Complexity Analysis: Time:O(n)    Space:O(k)
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        window = set()
        for i in range(n):
            if j - i > k:
                window.remove(nums[i])
                i +=1
            if nums[j] in window:
                return True
            window.add(nums[j])
        return False  
# Example Walkthrough
# Input: nums = [1, 2, 3, 1], k = 3
# Step	j	window	Action
# 1 	0	{}	    add 1 → {1}
# 2	    1	{1}	    add 2 → {1,2}
# 3	    2	{1,2}	add 3 → {1,2,3}
# 4	    3	{1,2,3}	1 already present → return True

# -----------------------------------------------------------------------------------
# 643. Maximun Average Subarray I
#  https://leetcode.com/problems/maximum-average-subarray-i/description/
# Approach: Check every subarray of size k, calculate its sum, and keep track of the maximum sum found. Finally, divide the maximum sum by k to get the maximum average.
# Complexity Analysis: Time: O(n × k)  Space: O(1)
class Solution:
    def findMaxAverage(self, nums, k):
        maxSum = float('-inf')
        for i in range(len(nums) - k + 1):
            currSum = 0 
            for j in range(i, i+1):
                currSum += nums[j]
            maxSum = max(maxSum, currSum)
        return maxSum / k
# Example Walkthrough: nums = [1,12,-5,-6,50,3], k = 4
# Subarray [1,12,-5,-6] → sum = 2
# Subarray [12,-5,-6,50] → sum = 51
# Subarray [-5,-6,50,3] → sum = 42
# Max sum = 51, average = 51 / 4 = 12.75

# Approach: First calculate the sum of the first k elements. Then slide the window by adding the next element and removing the leftmost element. Track the maximum window sum and divide by k at the end.
# Complexity Analysis: Time: O(n)   Space: O(1)
class Solution:
    def findMaxAverage(self, nums, k):
        windowSum = sum(nums[::k])
        maxSum = windowSum
        for i in range(k, len(nums)):
            windowSum += nums[i] # add next element
            windowSum -= nums[i-k] # remove leftmost element
            maxSum = max(maxSum, windowSum)
        return maxSum / k
# Example Walkthrough: nums = [1,12,-5,-6,50,3], k = 4
# Initial window [1,12,-5,-6] → sum = 2
# Slide → [12,-5,-6,50] → sum = 51 (max)
# Slide → [-5,-6,50,3] → sum = 42
# Max sum = 51, average = 12.75

# -------------------------------------------------------------------------------------------------------------------------------
# 3. Longest Substring witthout Repeating CHaracters
#  https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Approach: For every starting index i, expand the substring to the right until a duplicate character is found. Use a set to track unique characters and update the maximum length.
# Complexity Analysis: Time=O(n^2) Space=O(n)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         maxLen = 0
#         for i in range(len(s)):
#             seen = set()
#             for j in range(i, len(s)):
#                 if s[j] in seen:
#                     break
#                 seen.add(s[j])
#                 maxLen = max(maxLen, j - i + 1)
#         return maxLen
# Example Walkthrough: Input: "abcabcbb"
# i = 0
# a → ab → abc (unique, length = 3)
# next a → duplicate → stop
# i = 1
# b → bc → bca (length = 3)
# i = 2
# c → ca → cab (length = 3)
# Final answer = 3

# Approach 2: We maintain a window with two pointers (left, right) that always contains unique characters. As we expand right, if a duplicate appears, we shrink the window from the left until the duplicate is removed. At each step, update the maximum window length.
# Complexity Analysis: Time: O(n) → each character added & removed once  Space: O(n) → set for unique characters
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         seen = set()
#         left = 0
#         maxLen = 0
#         for right in range(len(s)):
#             # Shrink window until duplicate is removed
#             while s[right] in seen:
#                 seen.remove(s[left])
#                 left += 1
#             seen.add(s[right])
#             maxLen = max(maxLen, right - left + 1)
#         return maxLen
# Example Walkthrough: Input: "abcabcbb"
# Step	    i	j	Window	Seen    Set	maxLen
# a	        0	0	"a"	    {a}	     1
# b 	    0	1	"ab"	{a,b}    2
# c 	    0	2	"abc"	{a,b,c}	 3
# a(dup)	1	3	"bca"	{b,c,a}	 3
# b(dup)	2	4	"cab"	{c,a,b}	 3
# c(dup)	3	5	"abc"	{a,b,c}  3
# b(dup)	5	6	"cb"	{c,b}	 3
# b(dup)	6	7	"b"	    {b}	    3
# ✔️ Answer = 3

# Approach: Hum sliding window use karte hain with two pointers i and j.Agar koi character repeat hota hai aur current window ke andar hai, toh left pointer i ko uske last index + 1 pe shift kar dete hain. Har step pe window length update karte hain.
# Complexity:  Time: O(n)  Space: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}   # stores last index of each character
        max_len = 0
        i = 0             # left pointer
        for j in range(len(s)):  # right pointer
            c = s[j]
            if c in char_index and char_index[c] >= i:
                i = char_index[c] + 1   # move left pointer
            char_index[c] = j
            max_len = max(max_len, j - i + 1)
        return max_len
# Example: "abba"
# j	char	i	window	max
# 0	a	0	a	1
# 1	b	0	ab	2
# 2	b	2	b	2
# 3	a	2	ba	2
# ✔️ Answer = 2

#---------------------------------------------------------------------------------------------------------------------
# 187. Repeated DNA Sequence
# https://leetcode.com/problems/repeated-dna-sequences/description/
# You’re given a string s representing a DNA sequence made up of letters 'A', 'C', 'G', and 'T'. Return all the 10-letter long sequences (substrings) that occur more than once in the string.
# Approach: Try every substring of length 10, add it to a list or map to count occurrences, then return those that appear more than once.
# Complexity: Time: O((n-10+1) × 10) → O(n)   Space: O(n)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = {}
        result = set()
        for i in range(len(s) - 10 + 1):
            seq = s[i:i+10]
            if seq in seen:
                seen[seq] += 1
                if seen[seq] == 2:
                    result.add(seq)
            else:
                seen[seq] = 1
        return list(result)
# Example Walkthrough: Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Substrings of length 10:
# "AAAAACCCCC" → count = 2  
# "CCCCCAAAAA" → count = 2  
# ...
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

# Approach 2: Use a hash set to keep track of sequences seen once and another set for sequences already added to the result. Slide a 10-length window over the string. When a sequence is seen the second time, add to the result set.
# Complexity: Time: O((n-10+1) × 10) → O(n)   Space: O(n)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()
        for i in range(len(s) - 9):
            seq = s[i:i+10]
            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)
        return list(repeated)
# Example:  Input: "AAAAAAAAAAA"
# Substrings of length 10:
# "AAAAAAAAAA" (from idx 0)
# "AAAAAAAAAA" (from idx 1)
# The substring "AAAAAAAAAA" repeats → output:
# ["AAAAAAAAAA"]

# Approach: Sliding Window + Rabin–Karp: We slide a window of length 10 across the string and compute a rolling hash for each substring instead of slicing strings repeatedly. Each character (A, C, G, T) is mapped to a number, and the hash is updated in O(1) time when the window moves. If a hash repeats, the corresponding substring is added to the answer.
# Complexity:  Time: O(n)  Space: O(n)
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if len(s) < 10:
            return []
        # Map DNA characters to numbers
        mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        base = 4
        mod = 10**9 + 7
        hash_val = 0
        seen = set()
        repeated = set()
        power = pow(base, 9, mod)  # base^(window_size - 1)
        for i in range(len(s)):
            # Add new character to rolling hash
            hash_val = (hash_val * base + mapping[s[i]]) % mod
            # Remove leftmost character when window exceeds size 10
            if i >= 10:
                hash_val = (hash_val - mapping[s[i - 10]] * power) % mod
            # Window size is exactly 10
            if i >= 9:
                if hash_val in seen:
                    repeated.add(s[i - 9 : i + 1])
                else:
                    seen.add(hash_val)
        return list(repeated)
# Example Walkthrough: Input  s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Rolling Window (size = 10)
# Window	Substring	Action
# 0–9	AAAAACCCCC	Hash stored
# 1–10	AAAACCCCCA	Hash stored
# ...	...	...
# 10–19	AAAAACCCCC	Hash repeats → add to result
# 15–24	CCCCCAAAAA	Hash repeats → add to result
# Output
# ["AAAAACCCCC", "CCCCCAAAAA"]

# Approach (Bitmask): Since DNA has only 4 characters, each can be encoded using 2 bits. We slide a window of size 10 and maintain a 20-bit integer using bit shifting. Each window’s bitmask uniquely represents the substring, so if a mask repeats, the substring is repeated.
# Complexity:  Time: O(n)  Space: O(n)
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if len(s) < 10:
            return []
        # 2-bit encoding
        mapping = {
            'A': 0,  # 00
            'C': 1,  # 01
            'G': 2,  # 10
            'T': 3   # 11
        }
        seen = set()
        repeated = set()
        mask = 0
        WINDOW_MASK = (1 << 20) - 1  # keep last 20 bits
        for i in range(len(s)):
            # Shift left by 2 bits and add new char
            mask = ((mask << 2) | mapping[s[i]]) & WINDOW_MASK
            # Start checking once window size is 10
            if i >= 9:
                if mask in seen:
                    repeated.add(s[i - 9 : i + 1])
                else:
                    seen.add(mask)
        return list(repeated)
# Example Walkthrough:
# Input
# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Encoding Example
# A → 00
# C → 01
# G → 10
# T → 11
# First Window: "AAAAACCCCC"
# Binary:
# 00 00 00 00 00 01 01 01 01 01
# ↓
# 00000000000101010101   (20 bits)
# → Stored in seen
# Later Window: "AAAAACCCCC" (again)
# Same 20-bit mask appears
# Added to repeated
# Final Output ["AAAAACCCCC", "CCCCCAAAAA"]

# --------------------------------------------------------------------------------------
# 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/
# Approach: Start from every index i, keep adding fruits until more than 2 distinct types appear. Track the longest valid subarray.
# Complexty Analysis: Time:O(n²) Space:O(1)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxFruits = 0
        n = len(fruits)
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(fruits[j])
                if len(seen) > 2:
                    break
                maxFruits = max(maxFruits, j - i + 1)
        return maxFruits
# Example (Brute Force)
# Input: fruits = [1, 2, 1, 2, 3]
# i = 0 → [1,2,1,2] ✅ (2 types)
# i = 0 → [1,2,1,2,3] ❌ (3 types → stop)
# max = 4
# i = 1 → [2,1,2] → length 3
# i = 2 → [1,2] → length 2
# ✔️ Final Answer = 4

# Approach: Hum sliding window use karte hain jisme window ke andar sirf 2 fruit types allowed hain. Right pointer expand karta hai, aur agar 2 se zyada types aa gaye toh left pointer se shrink karte hain. Har valid window pe maximum length update karte rehte hain.
# Complexty Analysis: Time:O(n) Space:O(1)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        i = 0
        maxFruits = 0
        for j in range(len(fruits)):
            count[fruits[j]] += 1
            while len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
            maxFruits = max(maxFruits, j - i + 1)
        return maxFruits
# Walkthrough:
# Input: fruits = [1, 2, 1, 2, 3]
# i	j	window	count	        valid?	max
# 0	0	[1]	    {1:1}	          ✅	    1
# 0	1	[1,2]	{1:1,2:1}	      ✅	    2
# 0	2	[1,2,1]	{1:2,2:1}	      ✅    	3
# 0	3	[1,2,1,2]	{1:2,2:2}     ✅    	4
# 0	4	[1,2,1,2,3]	{1,2,3}	      ❌	shrink
# 2	4	[1,2,3]	{1,2,3}	          ❌	shrink
# 3	4	[2,3]	{2,3}	          ✅	    4
# ✔️ Answer = 4

# ------------------------------------------------------------------------------
# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Problem : Count the number of subarrays of size k whose average ≥ threshold 👉 Average ≥ threshold ⇔ sum ≥ k × threshold
# Approach : Check every contiguous subarray of size k by calculating its sum from scratch and compare it with k × threshold. Count how many such subarrays satisfy the condition. This is simple but inefficient due to repeated sum calculations.
# Complexity: Time: O(n*k)  Space: O(1)
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        count = 0
        for i in range(len(arr) - k + 1):
            curr_sum = 0
            for j in range(i, i + k):
                curr_sum += arr[j]
            if curr_sum >= target:
                count += 1        
        return count
# Example
# arr = [2,2,2,2,5,5,5,8]
# k = 3, threshold = 4
# target = 12
# Window	Elements	Sum	Valid
# 0–2 	    [2,2,2]	     6	❌
# 1–3	    [2,2,2]	     6	❌
# 2–4	    [2,2,5]	     9	❌
# 3–5	    [2,5,5]	    12	✅
# 4–6	    [5,5,5]	    15	✅
# 5–7	    [5,5,8]	    18	✅
# ✅ Answer = 3

# Approach: First compute the sum of the initial window of size k, then slide the window to the right by adding the next element and removing the leftmost one. This avoids recomputing sums and efficiently checks all subarrays in linear time.
# Complexity: Time: O(n)  Space: O(1)
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        window_sum = sum(arr[:k])
        count = 0
        if window_sum >= target:
            count += 1
        for i in range(k, len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i - k]
            if window_sum >= target:
                count += 1        
        return count
# Walkthrough
# Initial window:
# [2,2,2] → sum = 6 ❌
# Slide step by step:
# Add	Remove	Window	Sum	Valid
# +2	-2	[2,2,2]	    6	❌
# +5	-2	[2,2,5]	    9	❌
# +5	-2	[2,5,5]	    12	✅
# +5	-2	[5,5,5]	    15	✅
# +8	-5	[5,5,8]	    18	✅

# -------------------------------------------------------------------------------------
# 1838. Frequency of the Most Frequent Element
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
# Complexity: Time:O(n^2) Space: O(sortingspace complexity)
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxS = 0
        for i in range(len(nums)):
            fSum = 0
            for j in range(i, len(nums)):
                fSum += nums[j]
                total = nums[j] * (j - i + 1)
                cost = total - fSum
                if cost > k:
                    break
                maxS = max(maxS, j - i + 1)      
        return maxS
# Example
# nums = [1, 2, 4]  k = 5
# After sorting: nums = [1, 2, 4]
# Step-by-step
# i = 0   j = 0
# Window: [1]
# Sum = 1
# Cost = 1*1 - 1 = 0 ✅
# max = 1   j = 1
# Window: [1,2]
# Sum = 3
# Cost = 2*2 - 3 = 1 ✅
# max = 2  j = 2
# Window: [1,2,4]
# Sum = 7
# Cost = 4*3 - 7 = 5 ✅
# max = 3
# i = 1  j = 1
# Window: [2] → cost = 0 ✅
# j = 2
# Window: [2,4]
# Cost = 4*2 - 6 = 2 ✅
# i = 2    j = 2
# Window: [4] → cost = 0 ✅
# Maximum frequency = 3

# Approach: Sort the array and use a sliding window where we try to make all elements equal to the rightmost value. Maintain the sum of the window to calculate how many increments are needed. If the required operations exceed k, shrink the window from the left. Key Formula: cost = nums[right] * window_size - window_sum
# Complexity: Time: O(n log n) (sorting) Space: O(1)
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        maxS = 0
        nums.sort()
        fSum = 0
        i = j = 0
        while j < len(nums):
            fSum += nums[j]
            while nums[j] * (j - i + 1) - fSum > k:
                fSum -= nums[i]
                i += 1
            maxS = max(maxS, j - i + 1)
            j += 1
        return maxS
# Example
# nums = [1, 2, 4]  k = 5
# After sorting: nums = [1, 2, 4]
# Step-by-step
# right = 0
# Window: [1]
# Sum = 1
# Cost = 1*1 - 1 = 0 ✅
# max = 1   right = 1
# Window: [1,2]
# Sum = 3
# Cost = 2*2 - 3 = 1 ✅
# max = 2  right = 2
# Window: [1,2,4]
# Sum = 7
# Cost = 4*3 - 7 = 5 ✅
# max = 3
# Window never becomes invalid, so no shrinking needed.
# Maximum frequency = 3

# --------------------------------------------------------------------------------------------------------