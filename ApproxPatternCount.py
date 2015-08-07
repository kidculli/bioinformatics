__author__ = 'Cullin'
from HammingDistance import calc_dist

def count(text,pattern, d):
    """
    returns number of occurrences of pattern with up to d mismatches in text

    Args:
        :param text(str): text to search through
        :param pattern(str): pattern to search for occurrences
        :param d(int): distance; the acceptable number of mismatches allowed in a candidate pattern
    :return:
        int
    """
    found = 0
    for i in range(0,len(text)-len(pattern)+1):
        word = text[i:i+len(text)]
        if calc_dist(pattern,word) <= d:
            found += 1

    return found

print count('CCGGCGCAGATCAACCGAGTACGGCGGGGAAACCAAGGATCCTGGAGGTGCATGCCCTGTCGCCTGTTGGCCGTGTTTAGTACGCCACGATGTTCGCCGGTCCTAAGTATTGGTATGTCAGGGAAGGGTAGGTAAGTCGTTACCCTCTACCGTATGTGCGTGTCGTAGCCGTTATCTGATTGACATGACCGAGAATGGTGGCGGTTAGTCACGGCTATCAGGAAACAGGGAGCTGTAGTGTCAATGTCGTACGTGTTATTTCGTATAACCCTAAGGCTTCCTTCTGTCCCATTAGAATAGAGACTGTCC','ATGTGCG',2)