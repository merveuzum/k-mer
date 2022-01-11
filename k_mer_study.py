# Firstly, the sequence is entered
sequence = "CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGGCCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGTTTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCAAATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCGGGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGACTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA"

two_mer= []
three_mer= []
four_mer= []
five_mer= []
six_mer= []
base = 'ATCG'

#Created 2-3-4-5-6 k-mers separately (it could not be created in a single cycle)
#2-mer
for a in base:
    base1 = a
    for b in base:
        two_mer.append(base1+b)
print(two_mer)

#3-mer
for a in base:
    base1 = a
    for b in base:
        base2 = base1 + b
        for c in base:
            three_mer.append(base2+c)
print(three_mer)

#4-mer
for a in base:
    base1 = a
    for b in base:
        base2 = base1 + b
        for c in base:
            base3 = base2 + c
            for d in base:
                four_mer.append(base3+d)
print(four_mer)

#5-mer
for a in base:
    base1 = a
    for b in base:
        base2 = base1 + b
        for c in base:
            base3 = base2 + c
            for d in base:
                base4 = base3 + d
                for e in base:
                    five_mer.append(base4 + e)
print(five_mer)

#6-mer
for a in base:
    base1 = a
    for b in base:
        base2 = base1 + b
        for c in base:
            base3 = base2 + c
            for d in base:
                base4 = base3 + d
                for e in base:
                    base5=base4 + e
                    for g in base:
                        six_mer.append(base5 + g)
print(six_mer)

#
#two_mer
for i in two_mer:
    count = 0
    for x in range(len(sequence)-1):
         if sequence[x] + sequence[x + 1] == i:
            count += 1
    print(i, count)
    #print(count)
print(' ')

#three_mer
for i in three_mer:
    count = 0
    for x in range(len(sequence)-2):
         if sequence[x] + sequence[x + 1] + sequence[x + 2]== i:
            count += 1
    print(i, count)
    #print(count)
print(' ')

#four_mer
for i in four_mer:
    count = 0
    for x in range(len(sequence)-3):
         if sequence[x] + sequence[x + 1] + sequence[x + 2] + sequence[x + 3]== i:
            count += 1
    print(i, count)
    #print(count)
print(' ')

#five_mer
for i in five_mer:
    count = 0
    for x in range(len(sequence)-4):
         if sequence[x] + sequence[x + 1] + sequence[x + 2] + sequence[x + 3] + sequence[x + 4]== i:
            count += 1
    print(i, count)
    #print(count)



