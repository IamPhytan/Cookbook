#
# Get divisor and modulo
# Often forgotten, often useful
#

a = 5
b = 3

n, m = divmod(a, b)

print(n)  # 1
print(m)  # 2


#
# Next multiple of a number n
# Used a lot in CodinGame Clash of Code
#

n = 3
idx = [*range(10)]
res = [a + (n - (a % n)) % n for a in idx]
print(idx)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(res)  # [0, 3, 3, 3, 6, 6, 6, 9, 9, 9]


#
# Show a multiplication
# Used in CodinGame Clash of Code
#

# Numbers to multiply
a = 500
b = 1300

# Second number => String
b_s = str(b)

# Small multiplications
mults = list(reversed([a * int(b_s[i]) * 10 ** (len(b_s) - i - 1) for i in range(len(b_s))]))
mults = [m for m in mults if m != 0]

# Strings to list
s = [str(a), b_s, "-", *map(str, mults), "-"]
s.append(str(sum(list(mults))))

# Add mult sign
s[1] = "x " + b_s

# Adjust right align
n = len(max(s, key=len))
s = [w.rjust(n, " ") for w in s]

# Horizontal bars
s[2] = s[-2] = n * "-"
print("\n".join(s))
