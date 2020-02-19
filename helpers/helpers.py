import urllib.request

## a collection of helper functions


def read_fasta(filename, output_format=1):
    # quickly pull data from files that are in FASTA format
    # if output_format = 0, return strings and ids together in one list
    # if output_format = 1, return strings and ids in separate lists
    # if output_format = 2, return a dictionary with strings as keys, ids as values
    # if output_format = 3, return a dictionary with strings as values, and ids as keys
    with open(filename, "r") as f:
        strings = []
        ids = []
        buf = ""
        for line in f:
            line = line.strip()
            if line[0] == ">":
                if buf != "":
                    strings.append(buf)
                    buf = ""
                ids.append(line[1:])
            else:
                buf += line

        # one final append
        strings.append(buf)

    if output_format == 0:
        return zip(ids, strings)
    elif output_format == 1:
        return ids, strings
    elif output_format == 2:
        return dict(zip(strings, ids))
    elif output_format == 3:
        return dict(zip(ids, strings))
    else:
        raise ValueError("output_format is not correct")


def protein_from_uniprot(uniprot_id, output_file):
    url = "http://www.uniprot.org/uniprot/" + uniprot_id + ".fasta"
    urllib.request.urlretrieve(url, output_file)
