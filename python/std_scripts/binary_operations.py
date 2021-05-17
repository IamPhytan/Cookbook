#
# Convert integer to list of bits using stdlib
# Used a lot in CodinGame Clash of Code
#
i = 55  # Integer
n_bits = 8  # Number of bits

# Binary number starting from LSB (0, ..., 128)
i_bin = [(i >> d) & 1 for d in range(n_bits)]
print(i_bin)


#
# Remove MSB (first bit) from number
#
a = 500

# Number of bits : a.bit_length()
# For 8 bits, 1 << 7 = 128 (the number representing the MSB)
a_without_MSB = a - (1 << (a.bit_length() - 1))
print(a_without_MSB)
