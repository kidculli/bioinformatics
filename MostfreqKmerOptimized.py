__author__ = 'Cullin'

def freq_words(text,kmer):
    freq_dict = dict()

    for i in range(0,len(text)):
        curr_word = text[i:i+kmer]
        if freq_dict.has_key(curr_word):
            freq_dict[curr_word] += 1
        else:
            freq_dict[curr_word] = 1

    key = max(freq_dict, key=freq_dict.get)
    return (key,freq_dict[key])

print freq_words("CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA",3)