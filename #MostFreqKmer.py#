__author__ = 'Cullin'
import PatternCount

def freq_words(text,kmer):
    max_count = 0
    freq_words_dict = {}

    for i in range(0,len(text)-kmer + 1):
        word = text[i:i+kmer]
        freq = PatternCount.pattern_count(text,word)
        if freq >= max_count:
            max_count = freq
            freq_words_dict[word] = freq

    for k,v in freq_words_dict.items():
        if v < max_count:
            del freq_words_dict[k]

    return freq_words_dict

print freq_words("Cat in Hat Hat",3)