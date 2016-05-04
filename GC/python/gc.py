"""Rosalind Problem: Computing GC Content (GC)"""

import sys

def gc_content(dna):
    """
    Returns percenct gc content of given DNA string.
    """
    total_count = len(dna)
    gc_count = sum([1 for c in dna if c == 'G' or c == 'C'])
    return float(gc_count) / float(total_count) * 100

def max_gc_content():
    """
    Returns label and gc content for
    dna string with greatest gc content.
    """
    label = max_label = ''
    gc = max_gc = 0
    for line in sys.stdin:
        if line[0] == '>':
            if label:
                gc = gc_content(dna)
                if gc > max_gc:
                    max_label, max_gc = label, gc

            dna = ''
            label = line.strip()[1:]
        else:
            dna += line.strip()

    # process last dna strand
    gc = gc_content(dna)
    if gc > max_gc:
        max_label, max_gc = label, gc

    return max_label, max_gc

if __name__ == '__main__':
    label, gc = max_gc_content()
    print(label)
    print(gc)
