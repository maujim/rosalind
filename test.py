from helpers import helpers

filename = "mprt_temp.txt"

ids, data = helpers.read_fasta(filename, 1)

print(ids, data, sep="\n")
