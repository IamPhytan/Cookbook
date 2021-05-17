from collections import deque
import random

#
# Add numbers to queue alternatively
# Start : LRLRLRLR ("L")
#         RLRLRLRL ("R" or not "L")
# Order : min -> max ("D")
#         max -> min (not "D")
# Used in CodinGame Clash of Code
#
start, order = "R", "D"
values = [*range(15)]
N = sorted(random.sample(values, len(values)))
if order == "D":
    N.reverse()

nums = iter(N)
queue = deque([next(nums)])
left = start == "L"

for v in nums:
    if left:
        queue.appendleft(v)
    else:
        queue.append(v)
    left ^= 1

print(*queue)
