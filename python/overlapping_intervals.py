from functools import reduce

#
# Naive implementation of overlapping intervals merging
# used in CodinGame Clash of Code
#

# For each (min, max) get (min, max + 1)
intervals = [[4, 6], [1, 2], [10, 13], [0, 3], [7, 8]]
intervals = [[interv[0], interv[1] + 1] for interv in intervals]
# Get elements from intervals and put in set
intervals_sets = [set(range(*interval)) for interval in intervals]
# Unions inside
merged_intervals_elements = reduce(lambda x, y: x.union(y), intervals_sets)
print("Merged :", merged_intervals_elements)

# Global range of elements
min_number = min(merged_intervals_elements)
max_number = max(merged_intervals_elements)
all_numbers = set(range(min_number, max_number + 1))

not_included = all_numbers - merged_intervals_elements
print("Not included :", not_included)
