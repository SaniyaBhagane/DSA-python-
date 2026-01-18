1️⃣ 𝐓𝐰𝐨 𝐏𝐨𝐢𝐧𝐭𝐞𝐫𝐬 → when logic moves from both ends
If you’re working with a sorted array or string and comparing or merging from both sides, this pattern fits.
Triggers you’ll notice:
 • find pairs
 • remove duplicates
 • reverse in place
Replaces nested loops with clean O(n) logic.

2️⃣ 𝐁𝐢𝐧𝐚𝐫𝐲 𝐒𝐞𝐚𝐫𝐜𝐡 → when you’re searching for a value, not an element
Use this when the problem asks to minimize or maximize something over a sorted range.
Common triggers:
 • first / last position
 • minimum steps
 • “can we achieve X?”
Each step halves the search space → O(log n).

3️⃣ 𝐇𝐚𝐬𝐡𝐢𝐧𝐠 → when order doesn’t matter, existence does
Whenever you care about presence or frequency, use Sets or Maps.
Triggers:
 • unique elements
 • duplicates
 • group by
 • anagrams
Turns brute force checks into O(n).

4️⃣ 𝐒𝐥𝐢𝐝𝐢𝐧𝐠 𝐖𝐢𝐧𝐝𝐨𝐰 → when the word contiguous appears
Subarrays, substrings, ranges — this is your signal.
Triggers:
 • longest / shortest
 • sum or product
 • unique substring
You slide the window — you don’t restart → O(n) instead of O(n²).

5️⃣ 𝐒𝐭𝐚𝐜𝐤 / 𝐐𝐮𝐞𝐮𝐞 → when order or dependency matters
Stacks shine with previous–next or nested logic.
Queues work for sequential processing.
Triggers:
 • next greater element
 • balanced parentheses
 • undo / redo

6️⃣ 𝐑𝐞𝐜𝐮𝐫𝐬𝐢𝐨𝐧 → when the problem defines itself
If a task breaks into smaller versions of the same task, recursion fits naturally.
Triggers:
 • tree traversal
 • nested lists
 • divide and conquer
Always think: base case + sub
