__author__ = 'Cullin'
import FreqWordMismatch
import HammingDistance
import sys
import itertools

def find_motifs(dna,k,d):
    """
    Finds possible motifs for a list of dna sequences of length k and up to d mismatches
    Args:
        :param dna(list): list of dna sequences(str)
        :param k(int): length of kmer to look for
        :param d(int): max number of mismatches allowed
    :return:
        set() of motifs
    """
    motifs = set()
    dna_concat = ''.join(dna)
    for i in range(0,len(dna_concat) - k + 1):
        word = dna_concat[i:i+k]
        kmers = FreqWordMismatch.generate_kmers(word,d)
        for kmer in kmers:
            if all([FreqWordMismatch.count(seq,kmer,d) for seq in dna]):
                motifs.add(kmer)
    return motifs

def find_median(dna,k):
    kmers = set()
    ret_kmers = list()
    dna_concat = ''.join(dna)
    for i in range(0,len(dna_concat) - k + 1):
        word = dna_concat[i:i+k]
        kmers.add(word)

    min_dist = sys.maxint

    for kmer in kmers:
        dist = 0
        for others in kmers:
            dist += HammingDistance.calc_dist(kmer,others)
        print dist
        if dist < min_dist:
            ret_kmers = list()
            min_dist = dist
            ret_kmers.append(kmer)

        elif dist == min_dist:
            ret_kmers.append(kmer)

    return ret_kmers

def dist_between_patt_str(pattern,strings):
    distance = 0

    for string in strings:
        max_d = sys.maxint
        for i in range(0,len(string)-len(pattern) + 1):
            word = string[i:i + len(pattern)]
            curr_d = HammingDistance.calc_dist(pattern,word)
            if max_d > curr_d:
                max_d = curr_d

        distance += max_d

    return distance


def median_string_brute(dna,k):
    dist = sys.maxint
    median = ''
    y = list(itertools.product('ACTG', repeat = k))
    actual = [''.join(x) for x in y]
    for kmer in actual:
        the_dist = dist_between_patt_str(kmer,dna)
        if dist > the_dist :
            dist = the_dist
            median = kmer

    return median


def main():
    # x = ['AAGTAAGCAAAGTATTCCCAGCGCC','TACAGGCCCATGAAGGTCAAAAAGT','TACACAGGGCAAATAACCCATTTTT','ATTAGCATTAGCCCAAAGCTTGGCT','AAAAACAATGTTTGGACCCATTTAG','ATTCTACCCATCAATCGCATAGCGA']
    # y = find_motifs(x,5,1)
    # y = sorted(y)
    # for i in y:
    #     print i,
    # x = ['AAATTGACGCAT','GACGACCACGTT','CGTCAGCGCCTG','GCTGAGCACCGG','AGTTCGGGACAG']
    # print find_median(x,3)

    # x = ['TTACCTTAAC', 'GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG','CGTCAGAGGT']
    #
    # print 'distance:',dist_between_patt_str('AAA',x)
    x = ['CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC',
         'GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC',
         'GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG']


    print median_string_brute(x,7)

main()