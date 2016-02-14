s = 'GCTCATGGTGGGTACCCTGGCGTTAAGTCCGGGACCTGGGGTAAAATAGAAATACCGTCCCGAGAAGTCGAATATGGGATGGTACCCTCCCCTATACGTTTGGTGTTAACCGCCGTCGTCGCCTGAGTGATTGGGGTCCTGTCGCCGCGATATACTCTAGGTTAACTCAGGGACCCCACGGGACTATACTCGACTTGAAACCACTTTATCGAGTTTTGCTCTTAGTATAATGTTGCTTGTACAGAGGCACTTCATATGGTAACCAACATAGGTGAAGGCCCGCGGCCCAGGGTATTTCGGTCCTATGAATTAATCACAAGGGTCCCCCAGTTTCCGGGCTGGGAGGGCGCGGATGCTTTATCCCACTTTCTAAACACGATGTACTAATCCCACAATGGGTCTGACGCATAGCTAGGGTCAAACAGCATTCCGAGGTTCCTACGCGAGCTGTTAGCTTCTAACGCAATCCTTTTACTTCTAAGCAGCATATCACCACCTGCTGTATCTAGGTCAACCCTAGTATGTGGCGCGCTTAGGCAGGTCATCATTCTATCTGCCCCTTCTAACGCCTTTGGGATAATCGTGGCAATCGAGAACCACTGGTAGCTATTGCGCATAATCGATCGCGTTACTCACGGACACGAAAACTAACTTGTATTGTTGAGAAATCGACATCTTGGTAAGTCTCAGATAGTTCTGTTGGAAAAGCGGAGAATGATGCCCTAATAGAATCGGGTGCGGTGCAAGAGCATACTGCAGGCAGAGATCAGCGCTGCCCCTATTCGGATCATGCACTGGGCCGATTGTGGATTGTTATAAGCCATCGTACGGTTATGCCTGAACTCCGCACGAGTAGCCGCTAAGTTTTTACGAACTACTAATTAAAACAACTATGTCTTGAAGAAGTCCTGTCGACGTTAATTATT'
t = 'GCCGGAGGTGGAGTCAAGACATTTATGTCGGGGGCTTGGTACCGACGGGATCCGCGACCCCTAAAAAGCCCATTCATGCAGGGGCACACCCAAACATAAGTGCACTATCGCGGCGTGGTCGCACTGTTGAAAGATCTCACTTCTGAGTAGTTTCCCTTGTGTTCAACCCGTGACTCAAGATGATTTTTCAAGCCGAAAATACTCGTCAAAGCCAGTCACGTTAAATATAAAATCGCGCGCAGACGCTCCGATAACAGAGCACTCCAACTACTCCCCGGTCATTTAAATAGCCGCCTTCGGTGGTTCGACTTGAAAACCAGTGACTACCGAACTCGGTACAAGGCCGGCGCCGCCGTTCGAGCACACTAGCTAGCACCCATCTTATATCCCCAATTTACCTCTAACCTCTGGCTAGGCAGATTCTGCAGCGCAAGCGTTCTACACAATTGTTTAGTTTCTAAGGCCATCCTTTTTCGGCTACCCAGAAATCTACTACGTGAAGCAGAGAGATCTACCTTACGGCTAGGCGCCCCGCGTTGCGTCCATAGTGTATCCCCTCTAAATGACGTCGCAAGTCTCAGCGCCAAACATCAAAAGCCCGCGTAGCAGGAGGGTCTCCTTGGGAGCATAATACGGGGATGCGAGACTCAACGCGGTATTCGGCGCAAGCGTCATAGCGCCACTTCACAGGCAGCTTTGATTCTTATGACTGAGTAGCCTGACCCTAAGTACCGAGCGCGTGTCATCTTTGCAAGGACACTACAGATTGACGCTGCTCCACTTTAGATCGACAGGTGCACCTACTTCTGGTTACGATAACTCAGTCTACATCTACGCCTGTGCTCATCGGGGGTATCCGTCCCGTATTTACGAACTAATAATTAAAAGAGATCGTCAACAAAGAGACACCATTGACGTACTCTATC'

"""
Given two strings ss and tt of equal length, the Hamming distance between s and t,
denoted dH(s,t) is the number of corresponding symbols that differ in s and t.
"""
def get_hamming_distance(s, t):
    hamming_distance = 0
    s = list(s)
    t = list(t)

    while s:
        if s.pop() != t.pop():
            hamming_distance += 1

    return hamming_distance

print get_hamming_distance(s, t)