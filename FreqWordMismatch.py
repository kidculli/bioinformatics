__author__ = 'Cullin'
import itertools
from ApproxPatternCount import count
"""
Solution

Iterate text
For each word generate_kmers(word)
for each kmer if not in dict approxpatterncount(text,kmer,dist)
"""

def reverse_complement(seq):
    """

    :param
        seq(str): dna sequence
    :return:
        reverse complement of seq

    Raises:

        Raises Value Error if an improper seq is passed

    """
    seq = seq[::-1]
    seq = list(seq)
    for i,base in enumerate(seq):
        if base is 'A':
            seq[i] = 'T'
        elif base is 'T':
            seq[i] = 'A'
        elif base is 'G':
            seq[i] = 'C'
        elif base is 'C':
            seq[i] = 'G'
        else:
            raise ValueError("%s is not a valid base" % base)

    return ''.join(seq)

def check_equal(iterator):
    """
    # source : http://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
    Check to see if all values in the iterable container are equal i.e.  list, tuple

    :param
        iterator: iterable object
    :return:
        Bool
    """

    try:
        iterator = iter(iterator)
        first = next(iterator)
        return all(first == rest for rest in iterator)
    except StopIteration:
        return True

def generate_kmers(pattern,d):
    """
    returns all possible kmers for given pattern with up to d mismatches

    args:
        pattern(str) - pattern of bases
        d(int) - max number of mismatches allowed in kmers

    return:
        list()
    """

    # key = index of base in pattern, value  = list of the other possible bases for that position
    index_possibilities = dict()
    bases = set(['A','G','C','T'])
    # return list, initialize with pattern
    kmers = [pattern]

    if d < 1:
        return kmers

    for i, base in enumerate(pattern):
        temp = bases
        index_possibilities[i] = list(temp - set(base))

    # get all combinations of indices to change
    index_combos = list(itertools.combinations_with_replacement(range(0,len(pattern)),d))

    for combo in index_combos:
        temp = list(pattern)
        # case where all indexes are the same
        if check_equal(combo):
            index = combo[0]
            for base in index_possibilities[index]:
                temp[index] = base
                kmers.append(''.join(temp))

        else:
            # We need to build the expression statement
            arg_list = []
            for i in range(0,d):
                arg_list.append('index_possibilities[%d]' % i)
            arg = ','.join(arg_list)

            # Forward declaration
            cartesian_product = None
            # get cross product of the list of possible bases for each index
            exec 'cartesian_product = list(itertools.product(%s))' % arg

            for base_tuple in cartesian_product:
                for i, ind in enumerate(combo):
                    # set the index to new value
                    temp[ind] = base_tuple[i]

            kmers.append(''.join(temp))

    return kmers

def freq_words_mismatch(text, k, d):
    """
    Finds the most frequent kmer (including occurrences of its reverse complement) of length k with up to d mismatches
    in text.

    Args:
        :param text(str): text to search through
        :param k(int): length of kmer
        :param d(int): max number of mismatches allowed for possible kmer
    :return:
        list of most freq kmers of length k and with up to d mismatches found in text
    """
    freq_words = {}
    for i in range(0, len(text) - k + 1):
        word = text[i:i+k]
        kmers = generate_kmers(word,d)
        for kmer in kmers:
            if not freq_words.has_key(kmer):
                reverse = reverse_complement(kmer)
                found = count(text,kmer,d) + count(text,reverse,d)
                freq_words[kmer] = found

    maximum = max(freq_words.values())
    max_keys = [key for key,val in freq_words.items() if val == maximum]
    max_keys.append(maximum)
    return max_keys

#print freq_words_mismatch('ATATGCTGGTGGATTATAGCATTATAGCAGGCATGCGCTATGGATATAGATGCTAGCGCTAGCGCTGGAGGCTGGTAAGTGGGCGCGCGCTATGGATTATATAAGAGAGATATAGTGGATATGCTGGATATATATATTAATTGGGCAGGCATTATAAGAGATGCATATAGAGATTAGCAGAGAGATAGTGGGCATATTGGGC',7,3)

