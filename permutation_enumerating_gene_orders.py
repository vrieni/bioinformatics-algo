#http://rosalind.info/problems/perm/
#A permutation of length nn is an ordering of the positive integers {1,2,...,n}{1,2,...,n}.
#For example, pi=(5,3,2,1,4)pi=(5,3,2,1,4) is a permutation of length 55.

#Given: A positive integer n<=7.
#Return: The total number of permutations of length nn,
#followed by a list of all such permutations (in any order).


def permutation_yield(sequence):
    if len(sequence) == 0:
        yield []
    elif len(sequence) == 1:
        yield sequence
    else:
        l = []
        for i in range(len(sequence)):
            x = sequence[i]
            xs = sequence[:i] + sequence[i+1:]
            for p in permutation_yield(xs):
                yield [x] + p


data = list('12345')

print 'permutation'
ctr = 0
for p in permutation_yield(data):
    ctr += 1
    print ' '.join(str(i) for i in p)

print ctr


