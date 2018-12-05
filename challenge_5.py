from string import ascii_lowercase
# # In aA, a and A react, leaving nothing behind.
# # In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
# # In abAB, no two adjacent units are of the same type, and so nothing happens.
# # In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
#
# dabAcCaCBAcCcaDA
# dabAaCBAcCcaDA
# dabCBAcCcaDA
# dabCBAcaDA <- it appears we read left to right


# How many units remain after fully reacting the polymer you scanned?

# part 1
INPUT = "./polymer.text"
letters = open(INPUT).read().strip()
list_letters = list(letters)
# list_letters = ['d','a','b','A','c','C','a','C','B','A','c','C','c','a','D','A']
def react_a_list(list_letters):
    found = True
    i = 0
    while found == True:
        for x in range(i, len((list_letters))-1):
            #print(" checking " +  str(list_letters[x]) + " at place " + str(x))
            if list_letters[x].lower() == list_letters[x+1].lower():
                if (list_letters[x].isupper() and list_letters[x+1].islower()) or (list_letters[x+1].isupper() and list_letters[x].islower()):
                    # delete both and restart loop
                    # print ("delete " + str(list_letters[x]) +  " and " + str(list_letters[x+1]) + " at place "  + str(x) + " and " + str(x+1))
                    i = max(x - 1, 0) # reset i to be the 0 or before the first of the deleted letters
                    del list_letters[x]
                    del list_letters[x]
                    break
        else:
            print("done")
            return len(list_letters)
            found = False

# part 2
# What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?

letter_redacted_count = {}
for c in ascii_lowercase:
    letters = open(INPUT).read().strip()
    # if the letter isn't there at all, skip it
    if c not in letters:
        continue
    else:
        letters = letters.replace(c.upper(), '').replace(c.lower(), '')
        list_letters = list(letters)
        letter_redacted_count[c] = react_a_list(list_letters)

for key, value in sorted(letter_redacted_count.iteritems(), key=lambda (k,v): (v,k)):
    print(key, value)
