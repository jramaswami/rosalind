"""Reverse complement of a Strand of DNA."""
import sys

def readbackwards(fp):
    """Generator to read a file backwards."""
    # Go to the end of the file
    fp.seek(0, 2)
    read_pointer = fp.tell()

    # Skip one trailing new line that appears
    # due to the EOF, I think (?)
    read_pointer -= 1
    if fp.read(1) == '\n':
        read_pointer -= 1

    while fp.tell() > 1:
        read_pointer -= 1
        fp.seek(read_pointer, 0)
        yield fp.read(1)

def complement(c):
    """Translates c to its complement"""
    map = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    if c in map:
        return map[c]
    else:
        return c

def main():
    """Main program."""
    for c in readbackwards(sys.stdin):
            print(complement(c), end="")

if __name__ == '__main__':
    main()
