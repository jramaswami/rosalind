"""Rosalind Problem 1: Counting DNA Nucleotides"""

import sys
import collections

def main():
    """Main program"""
    result = collections.defaultdict(int)
    for line in sys.stdin:
        line = line.strip()
        for nucleotide in line:
            result[nucleotide] += 1

    print(" ".join([str(result[k]) for k in ['A', 'C', 'G', 'T']]))

if __name__ == '__main__':
    main()
