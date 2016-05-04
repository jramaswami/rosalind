"""Transcribe DNA to RNA"""

import sys

def main():
    """Main program."""
    c = sys.stdin.read(1)
    while c:
        if c == 'T':
            print('U', end='')
        else:
            print(c, end='')
        c = sys.stdin.read(1)

if __name__ == '__main__':
    main()

