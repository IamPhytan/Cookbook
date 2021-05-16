#
# Convert integer to list of bits using stdlib
#
i = 55  # Integer
n_bits = 8  # Number of bits

# Binary number starting from LSB (0, ..., 128)
i_bin = [(i >> d) & 1 for d in range(n_bits)]
print(i_bin)
