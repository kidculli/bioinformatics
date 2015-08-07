__author__ = 'KidCulli'
# '*' is stop codon
aminoacids=\
    {"ATT":'Ile',"ATC":'Ile',"ATA":'Ile',"ATG":"Met",
     "GCA":"Ala","GCC":"Ala","GCG":"Ala","GCT":"Ala",
     "AAC":"Asx","AAT":"Asx","GAC":"Asx","GAT":"Asx",
     "TGC":"Cys","TGT":"Cys","GAC":"Asp","GAT":"Asp",
     "GAA":"Glu","GAG":"Glu","TTC":"Phe","TTT":"Phe",
     "GGA":"Gly","GGC":"Gly","GGG":"Gly","GGT":"Gly",
     "CAC":"His","CAT":"His","AAA":"Lys","AAG":"Lys",
     "CTA":"Leu","CTC":"Leu","CTG":"Leu","CTT":"Leu","TTA":"Leu","TTG":"Leu",
     "AAC":"Asn","AAT":"Asn","CCA":"Pro","CCC":"Pro","CCG":"Pro","CCT":"Pro",
     "CAA":"Gln","CAG":"Gln","ACA":"Thr","ACC":"Thr","ACG":"Thr","ACT":"Thr",
     "GTA":"Val","GTC":"Val","GTG":"Val","GTT":"Val","TGG":"Trp","TAC":"Tyr","TAT":"Tyr",
     "CAA":"Glx","CAG":"Glx","GAA":"Glx","GAG":"Glx","TAA":"*","TAG":"*","TGA":"*",
     "AGA":"Arg","AGG":"Arg","CGA":"Arg","CGC":"Arg","CGG":"Arg","CGT":"Arg",
     "AGC":"Ser","AGT":"Ser","TCA":"Ser","TCC":"Ser","TCG":"Ser","TCT":"Ser",
     }
def translate(codon):
    try:
        AA=aminoacids[codon]
    except KeyError:
        return "NNN"
    return AA
