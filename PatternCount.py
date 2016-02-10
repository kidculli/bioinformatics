__author__ = 'Cullin'
import pdb

def pattern_count(text,pattern):
    count = 0
    for i in range(0,len(text)-len(pattern)+1):
        #seg = text[i:i+len(pattern)]
        #print i, seg
        if text[i:i+len(pattern)] == pattern:
            count += 1

    return count

#pdb.set_trace()
print pattern_count('GACCATCAAAACTGATAAACTACTTAAAAATCAGT',"AAA")