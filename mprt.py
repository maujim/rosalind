import re
import operator
from functools import reduce
from helpers import helpers

# import data
with open("rosalind_mprt.txt", "r") as f:
    data = f.readlines()

filename = "mprt_temp.txt"
pattern = re.compile(r"N[^P][ST][^P]")

for access_id in data:
    access_id = access_id.strip()

    helpers.protein_from_uniprot(access_id, filename)
    _, sequence = helpers.read_fasta(filename, 1)

    sequence = sequence[0]
    matches = pattern.findall(sequence)
    # skip loop if no matches found
    if matches == []:
        continue

    interim = list(map(len, pattern.split(sequence)))

    # catches any matches that take place right at beginning or end of string
    assert len(matches) + 1 == len(interim)

    output = [interim[0] + 1]

    for i in range(1, len(interim)):
        a = interim[:i]
        b = reduce(operator.add, a)
        c = interim[i]
        d = 4 * i + c + b + 1
        output.append(d)

    print(access_id)
    print(*output[: len(matches)])
