def seq_gen (type):
    def arith_seq (seed, diff, terms):
        seq = []
        i = 1
        while i <= terms:
            seq.append(diff * (i - 1) + seed)
            i += 1
        else:
            seq_sum = sum(seq)
            print(f"Arithmetic sequence generated with {terms} terms")
            print(f"The sequence is {seq}")
            print(f"The sum of the sequence is {seq_sum}")
    def geo_seq (seed, ratio, terms):
        seq = []
        i = 1
        while i <= terms:
            seq.append(seed * (ratio ** i - 1))
            i += 1
        else:
            seq_sum = sum(seq)
            print(f"Geometric sequence generated with {terms} terms")
            print(f"The sequence is {seq}")
            print(f"The sum of the sequence is {seq_sum}")
    if type == "arithmetic":
        indata_a = int(input("Enter first term:"))
        indata_b = int(input("Enter common difference:"))
        indata_c = int(input("Enter number of terms:"))
        arith_seq(indata_a, indata_b, indata_c)
    else:
        indata_a = int(input("Enter first term:"))
        indata_b = int(input("Enter common ratio:"))
        indata_c = int(input("Enter number of terms:"))
        geo_seq(indata_a, indata_b, indata_c)
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("seq_type")
args = parser.parse_args()
seq_gen(args.seq_type)