#!/usr/bin/python3
"""
0-minoperations.py
"""
import shutil, os


def minOperations(n):
    """
    minOperations function returns the number of operations
    for n character
    """
    if n <= 1:
        return 0

    operations = 0
    # extraire les 2
    while n % 2 == 0:
        operations += 2  # facteur 2 coûte 2 opérations
        n //= 2

    # extraire les facteurs impairs
    p = 3
    while p * p <= n:
        while n % p == 0:
            operations += p  # facteur p coûte p opérations
            n //= p
        p += 2

    # s'il reste un facteur premier > 1
    if n > 1:
        operations += n

    return operations
