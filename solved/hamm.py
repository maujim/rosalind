import math

# import strings
with open('rosalind_hamm.txt', 'r') as f:
    inp_1 = f.readline()
    inp_2 = f.readline()

# mc = merge_compare
# recursively split strings into half and compare substrings. Continue recursion if substrings are different and stop otherwise.
def mc(s1, s2):
    if s1 is s2:
        return 0
    else:
        l = math.ceil(len(s1))
        count = 0
        count += mc(s1[:l], s2[:l])
        count += mc(s1[l:], s2[l:])
    
    return count


print(mc(inp_1, inp_2))
