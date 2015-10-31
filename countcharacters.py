import sys

dna = sys.stdin.read().strip()

counter = {'A': 0, 'C':0, 'G': 0, 'T': 0}

for i in dna:
    counter[i] = counter[i] + 1


print '%s %s %s %s' % (counter['A'], counter['C'], counter['G'], counter['T'])