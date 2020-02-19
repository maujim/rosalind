# import data
with open("rosalind_iprb.txt", "r") as f:
    data = f.readline().strip().split(" ")
    # k organisms of form YY
    k = int(data[0])
    # m organisms of form Yy
    m = int(data[1])
    # n organisms of form yy
    n = int(data[2])

t = k + m + n  # total

# Chance of producing offspring with dominant allele
# YY paired with anything: 1.0
# Yy paired with Yy      : 0.75
# Yy paired with yy      : 0.5
# yy paired with yy      : 0

a = (k / t) * sum([k - 1, m, n])
b = (m / t) * sum([k, 0.75 * (m - 1), 0.5 * n])
c = (n / t) * sum([k, 0.5 * m, 0 * n])

output = (1 / (t - 1)) * (a + b + c)

print(output)
