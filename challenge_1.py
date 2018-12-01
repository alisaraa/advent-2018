import sys

INPUT = "./frequency_values"

f = open(INPUT).read().splitlines()
total = 0
frequencies = {}
while True:
    for line in f:
        total = total + int(line)
        frequencies[total] = frequencies.get(total,0) + 1
        #print(frequencies)
        if frequencies[total] == 2:
            #print(frequencies)
            print(total)
            sys.exit(-1)
