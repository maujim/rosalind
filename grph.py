from helpers.helpers import read_fasta
from itertools import repeat

# import data
dict_data = read_fasta("rosalind_grph.txt", 2)
print(dict_data)
data = list(dict_data.keys())
k = 3


def comparison(compare_against, to_compare, p):
    if to_compare[-p:] == compare_against[:p]:
        return True
    else:
        return False


all_edges = []
for i in range(len(data)):
    comparison_str = data[i]
    intermediary = lambda x: comparison(x, comparison_str, k)
    temp_data = data[:i] + data[i + 1 :]
    edges = list(filter(intermediary, temp_data))
    if edges != []:
        for edge in edges:
            all_edges.append([dict_data[data[i]], dict_data[edge]])

with open("output.txt", "w") as f:
    for edge in all_edges:
        print(*edge, file=f)
