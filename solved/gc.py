# import data
with open("rosalind_gc.txt", "r") as f:
    lines = f.readlines()

fasta_id = ""
gc_content = 0.0
buf = ["", 0, 0]
gc_content_temp = 0
fasta_id_temp = ""

for line in lines:
    line = line.strip()
    if line[0] == ">":
        # compute gc
        if buf[1] != 0:
            gc_content_temp = 100 * buf[2] / buf[1]
        if gc_content_temp > gc_content:
            gc_content = gc_content_temp
            fasta_id = fasta_id_temp

        # reset buffer
        buf = ["", 0, 0]

        # update id
        fasta_id_temp = line[1:]

    else:
        # update buffer
        buf[0] = buf[0] + line
        buf[1] = len(buf[0])
        buf[2] = buf[0].count("G") + buf[0].count("C")

# need one more computation for last line
gc_content_temp = 100 * buf[2] / buf[1]
if gc_content_temp > gc_content:
    gc_content = gc_content_temp
    fasta_id = fasta_id_temp

print(fasta_id, gc_content, sep="\n")
