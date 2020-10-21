def main(seqType, firstTerm, terms, differenceRatio):
    def arith_seq (seed, difference, terms):
        seq = [(difference * (x - 1) + seed)]
        seq_sum = sum(seq)
        print(f"Arithmetic sequence generated with {terms} terms")
        print(f"The sequence is {seq}")
        print(f"The sum of the sequence is {seq_sum}")
    def geo_seq (seed, ratio, terms):
        seq = [(seed * (ratio ** x - 1)) for x in range(terms + 1)]
        seq_sum = sum(seq)
        print(f"Geometric sequence generated with {terms} terms")
        print(f"The sequence is {seq}")
        print(f"The sum of the sequence is {seq_sum}")
    if seqType == "arithmetic":
        arith_seq(firstTerm, differenceRatio, terms)
    else:
        geo_seq(firstTerm, differenceRatio, terms)
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--seqType", '-s', choices = ['arithmetic', 'geometric'])
parser.add_argument("--firstTerm", '-f', type = float)
parser.add_argument("--terms", '-t', type = int)
parser.add_argument("--differenceRatio", '-dr', type = float)
args = parser.parse_args()
seqType = args.seqType
firstTerm = args.firstTerm
terms = args.terms
differenceRatio = args.differenceRatio
main(seqType, firstTerm, terms, differenceRatio)
