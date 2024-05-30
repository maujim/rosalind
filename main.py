from collections import Counter
import unittest
import sys, pathlib

def dna(s: str) -> str:
    c = Counter(s)
    acgt = [c['A'], c['C'], c['G'], c['T']]
    return ' '.join(map(str, acgt))

def rna(t: str) -> str:
    u = t.replace('T', 'U')
    return u

def revc(s: str) -> str:
    s = s.replace('\n', '')
    reversed = s[::-1]
    d = {'A': 'T', 'T': 'A', 'C':'G', 'G':'C'}
    return ''.join( d[x] for x in reversed)

class TestSolutions(unittest.TestCase):
    def test_dna(self):
        test_input = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        test_ans = "20 12 17 21"
        self.assertEqual(dna(test_input), test_ans)

    def test_rna(self):
        test_input = "GATGGAACTTGACTACGTAAATT"
        test_ans = "GAUGGAACUUGACUACGUAAAUU"
        self.assertEqual(rna(test_input), test_ans)

    def test_revc(self):
        test_input = "AAAACCCGGT"
        test_ans = "ACCGGGTTTT"
        self.assertEqual(revc(test_input), test_ans)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        unittest.main(verbosity=2)
    elif len(sys.argv) == 3:
        rosalind_id : str = sys.argv[1].lower()
        file = sys.argv[2]

        target_fn = locals()[rosalind_id]

        p = pathlib.Path(file)
        with p.open('r') as fp:
            input = fp.read()

        output = target_fn(input)
        print(output)
    else:
        sys.exit("unknown numbers of arguments")
