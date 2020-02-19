# import data
with open("rosalind_subs.txt", "r") as f:
    inp_1 = f.readline().strip()
    inp_2 = f.readline().strip()

r = 0
output = [0]

while True:
    inp_1 = inp_1[r:]

    r = inp_1.find(inp_2)

    if r == -1:
        break

    r += 1
    output.append(r + output[-1])

print(*output[1:])
