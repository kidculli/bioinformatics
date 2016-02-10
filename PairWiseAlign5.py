__author__ = 'Cullin'
"""
File: PairWiseAlign.py
Created on: 2016-01-30
Updated on 2016-02-10

This file implements pairwise alignment procedure of two dna sequences

python 2.7.1
"""

from collections import namedtuple
# use numpy array matrix
import numpy as np

# Scoring Scheme used to award points for match/mismatch
SCORING_SCHEME = {'T':{'T':20,'C':10,'A':5,'G':5},
                  'C':{'C':20,'T':10,'A':5,'G':5},
                  'G':{'G':20,'A':10,'T':5,'C':5},
                  'A':{'G':10,'A':20,'T':5,'C':5}}
# Gap Penalty
GAP_PEN = -5
# Declaration of Global Scoring Matrix
SCORING_MATRIX = None
# Declaration of list of possible alignment paths
THE_PATH = list()

# Create named tuple
Coordinate = namedtuple('Coordinate','direction coordinate')
NULL_DIRECTION = Coordinate('NONE',None)
# value = score , direction key: hori, vert, diag val: coordinate
# directions is a list of Coordinates
Origin = namedtuple('Origin','value directions')

def custom_max(hori,vert,diag):
    """
    This function compares the values of 3 positions on the scoring matrix in relation to the current position
    and returns a dict of the max value along with a list of directions yielding the max

    :param hori: value of horizontal position on grid
    :param vert: value of vertical position on grid
    :param diag: value of diagonal position on grid
    :return: dict with key of max value and list of directions
    """
    # get passed in args
    args = locals()
    # list of dict of highest scores
    high_scores =[]
    # get max val
    max_val = max(hori,vert,diag)
    for key, arg in args.iteritems():
        if arg == max_val:
            high_scores.append(key)

    return {max_val:high_scores}

def trace_back(position,path_list):
    """
    Recursively trace back paths from last position in the SCORING MATRIX

    :param position: value of type Origin Tuple()
    :param seq1: list to contain trace back paths
    :return: Update global SCORING_MATRIX
    """
    # If we reach the end of the path append this path to the global THE_PATH list and return
    if position.directions[0].coordinate == None:
        THE_PATH.append(path_list)
        return
    # call function again for each path in the possible directions list, update path_list
    else:
        for path in position.directions:
            trace_back(SCORING_MATRIX[path.coordinate[0],path.coordinate[1]],path_list + [(path.coordinate,path.direction)])

def align(seq1,seq2):
    """
    Prints out all possible alignments of seq1 and seq2
    :param seq1: string of DNA
    :param seq2: string of DNA
    """
    # last matrix position
    last_ind = (len(seq1),len(seq2))
    # build the scoring matrix
    build_score_matrix(seq1,seq2)
    # trace back the paths on the scoring matrix
    trace_back(SCORING_MATRIX[last_ind[0]][last_ind[1]],list())
    # build alignment for each possible path
    for path in THE_PATH:
        # initial vars
        align_seq1 = ''
        align_seq2 = ''
        # pos of last char of the seqs
        curr_seq1_pos = len(seq1)-1
        curr_seq2_pos = len(seq2)-1
        # build alignment strings based on origin direction
        for point_tup in path:
            direction = point_tup[1]
            if direction == 'diag':
                align_seq1 = seq1[curr_seq1_pos] + align_seq1
                curr_seq1_pos -= 1
                align_seq2 = seq2[curr_seq2_pos] + align_seq2
                curr_seq2_pos -= 1
            elif direction == 'vert':
                align_seq1 = seq1[curr_seq1_pos] + align_seq1
                curr_seq1_pos -= 1
                align_seq2 = '-' + align_seq2
            elif direction == 'hori':
                align_seq2 = seq2[curr_seq2_pos] + align_seq2
                curr_seq2_pos -= 1
                align_seq1 = '-' + align_seq1
        # Terminating position of path on matrix
        fin_point = path.pop()[0]
        # if index negative we need to fill leading '-' based on terminating position coordinates
        # if positive we need to fill in the rest of the chars in the seq
        if curr_seq1_pos < 0:
            align_seq1 = ("-" * fin_point[1]) + align_seq1
        else:
            align_seq1 = seq1[:curr_seq1_pos + 1] + align_seq1
        if curr_seq2_pos < 0:
            align_seq2 = ("-" * fin_point[0]) + align_seq2
        else:
            align_seq2 = seq2[:curr_seq2_pos + 1] + align_seq2

        # output aligned seqs
        print align_seq2
        print align_seq1
        print '*****************************'

def build_score_matrix(seq1,seq2):
    """
    Builds scoring matrix from 2 inputted dna seqs
    updates global SCORING_MATRIX

    :param seq1: dna seq 1
    :param seq2:  dna seq 2
    :return: numpy array scoring matrix
    """
    # dt = np.int32
    dt = np.dtype(Origin)
    # initialize 2d array of ints
    the_matrix = np.array([[]],dtype=dt)
    # resize 2d array
    the_matrix.resize((len(seq1)+1,len(seq2)+1))
    # insert first row gap pen
    the_matrix[0]=[Origin(i * GAP_PEN,[NULL_DIRECTION]) for i in range(0,len(seq2)+1)]
    # insert first col gap pen
    the_matrix[:,0] = [Origin(i * GAP_PEN,[NULL_DIRECTION]) for i in range(0,len(seq1)+1)]
    #iterate through and build scoring matrix
    for i in range(1,len(seq1)+1):
        for j in range(1,len(seq2)+1):
            # get the max values
            max_values = custom_max(the_matrix[i][j-1].value + GAP_PEN,the_matrix[i-1][j].value + GAP_PEN,
                                    SCORING_SCHEME[seq1[i-1]][seq2[j-1]] + the_matrix[i-1][j-1].value)

            # initialize possible directions list
            direction_list =[]
            for direction in max_values.values()[0]:
                if direction == 'hori':
                    direction_list.append(Coordinate(direction,(i,j-1)))
                elif direction == 'vert':
                    direction_list.append(Coordinate(direction,(i-1,j)))
                elif direction == 'diag':
                    direction_list.append(Coordinate(direction,(i-1,j-1)))
            # update matrix index with score value and directions list
            the_matrix[i][j] = Origin(max_values.keys()[0],direction_list)

    # update global Scoring Matrix
    global SCORING_MATRIX
    SCORING_MATRIX = the_matrix

    return the_matrix





if __name__ == '__main__':
    align('ATG','GGAAT')



