__author__ = 'Cullin'
def calc_skew(genome,length):
    current_skew = 0
    # Initialize first index with 0 for some reason
    skew_list = [0]
    for i in range(0,length):
        if genome[i] is 'G':
            current_skew += 1

        elif genome[i] is 'C':
            current_skew -=1

        skew_list.append(current_skew)

    return skew_list

def calc_min_skew(genome,length):
    min_val = 0
    min_indices = []
    skews = calc_skew(genome,length)
    for i in range(0,length):
        if skews[i] < min_val:
            min_val = skews[i]
            min_indices = [i]

        elif skews[i] == min_val:
            min_indices.append(i)

    return (min_val,min_indices)


text = 'GATACACTTCCCGAGTAGGTACTG'

print calc_min_skew(text,len(text))
# result =  calc_skew(text,len(text))
# print len(result)
# print(result)

#0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2