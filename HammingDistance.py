__author__ = 'Cullin'
def calc_dist(string1,string2):
    """
    Returns the Hamming Distance of two sequences
    Args
        :param string1(str): a dna seq
        :param string2(str): a dna seq
    :return:
        int
    """
    distance = 0
    for i in range(0,len(string1)):
        if string1[i] != string2[i]:
            distance += 1

    return distance

# x = 'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
# y = 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'
# print calc_dist(x,y)