"""Rosalind problem: FIB"""

import sys

def fib(n, k):
    """Calculate fibonacci number."""
    if n == 0:
        return 0
    elif n < 2:
        return 1
    else:
        return fib(n - 1, k) + (k * fib(n - 2, k))

def main() :
    """Main program"""
    for line in sys.stdin:
        n, k = map(int, line.strip().split())
        print(fib(n, k))

if __name__ == '__main__':
    main()
