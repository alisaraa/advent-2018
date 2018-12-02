from collections import Counter
INPUT = "./box_ids.text"

## seed the checksum dict
checksum = {'2': 0, '3': 0}

f = open(INPUT).read().splitlines()
## count those with 2 of the same letter and/or 3 of the same letter

for line in f:
    ## for each entry, create a dict of letters
    alpha_dict = {}
    for letter in line:
        alpha_dict[letter] = alpha_dict.get(letter, 0) + 1
    for key, value in alpha_dict.iteritems():
        if value == 2:
            checksum['2'] = checksum.get('2', 0) + 1
            break
    for key, value in alpha_dict.iteritems():
        if value == 3:
            checksum['3'] = checksum.get('3', 0) + 1
            break
## challenge part 1: find checksum
print(checksum['2'] * checksum['3'])

## challenge part 2: find same boxes
line_no = 0
for line in f:
    line_no = line_no + 1
    for next_line in f[line_no:]:
        mismatch_array = []
        mismatch = 0
        letters = 0
        while letters < len(line):
            if line[letters] != next_line[letters]:
                mismatch = mismatch + 1
            else:
                mismatch_array.append(line[letters])
            letters = letters + 1
        if mismatch == '1' or mismatch == 1:
            print(''.join(mismatch_array))
