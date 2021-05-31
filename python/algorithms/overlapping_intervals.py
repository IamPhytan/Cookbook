from functools import reduce
import operator

#
# Naive implementation of overlapping intervals merging
# used in CodinGame Clash of Code
#

# For each (min, max) get (min, max + 1)
intervals = [[4, 6], [1, 2], [10, 13], [0, 3], [7, 8], [5, 8]]
intervals_shift = [[interv[0], interv[1] + 1] for interv in intervals]

# Get elements from intervals and put in set
intervals_sets = [set(range(*interval)) for interval in intervals_shift]
# Unions inside
merged_intervals_elements = reduce(lambda x, y: x.union(y), intervals_sets)
print("Merged :", merged_intervals_elements)

# Global range of elements
min_number = min(merged_intervals_elements)
max_number = max(merged_intervals_elements)
all_numbers = set(range(min_number, max_number + 1))

not_included = all_numbers - merged_intervals_elements
print("Not included :", not_included)


#
#  Merge intervals less naively
#

# Converts interval to set
interval_to_set = lambda i: set(range(i[0], i[1] + 1))

# Sorted list of intervals / sets
sorted_interv = sorted(intervals, key=operator.itemgetter(0, 1))
sorted_sets = [interval_to_set(interv) for interv in sorted_interv]

# Merged intervals
merged_intervals = [sorted_interv[0]]

for idx, (interval, interval_set) in enumerate(zip(sorted_interv[1:], sorted_sets[1:])):
    # Last interval to be merged
    last_known_interval = merged_intervals[-1]
    last_known_set = interval_to_set(last_known_interval)
    if interval_set.issubset(last_known_set):
        # Interval is already included
        continue
    elif interval_set.isdisjoint(last_known_set):
        # New interval with unseen elements
        merged_intervals.append(interval)
        continue
    else:
        # New interval is partly contained in last known interval
        # Change end of last interval to end of new interval
        merged_intervals[-1][-1] = interval[-1]


print("Merged Intervals :", " ".join("-".join(map(str, interval)) for interval in merged_intervals))
