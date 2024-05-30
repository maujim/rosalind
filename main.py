from collections import Counter
import unittest
import inspect
import timeit
import functools, re
import sys, pathlib


def dna(s: str) -> str:
    assert len(s) < 1001

    c = Counter(s)
    acgt = [c["A"], c["C"], c["G"], c["T"]]
    return " ".join(map(str, acgt))


def rna(t: str) -> str:
    assert len(t) < 1001

    u = t.replace("T", "U")
    return u


def revc(s: str) -> str:
    assert len(s) < 1001

    s = s.replace("\n", "")
    reversed = s[::-1]
    d = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(d[x] for x in reversed)


def fib(n: int, k: int) -> int:
    assert n < 41
    assert k < 6

    @functools.cache
    def inner_fib(n2):
        if n2 == 1 or n2 == 2:
            return 1
        return inner_fib(n2 - 1) + k * inner_fib(n2 - 2)

    return inner_fib(n)


class TestSolutions(unittest.TestCase):
    def test_dna(self):
        test_input = (
            "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        )
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

    def test_fib(self):
        n = 5
        k = 3
        test_ans = 19
        self.assertEqual(fib(n, k), test_ans)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        unittest.main(verbosity=2)
    elif len(sys.argv) == 3:
        rosalind_id: str = sys.argv[1].lower()
        file = sys.argv[2]

        target_fn = locals()[rosalind_id]

        p = pathlib.Path(file)
        with p.open("r") as fp:
            input = fp.read()

        # special cases
        if rosalind_id == "fib":
            m = re.search(r"(\d+) (\d+)", input)
            n = int(m.group(1))
            k = int(m.group(2))
            print(n, k)
            output = target_fn(n, k)
        else:
            output = target_fn(input)
        print(output)
    else:
        sys.exit("unknown numbers of arguments")
