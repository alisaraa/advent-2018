
INPUT = "./fabric_dimensions.text"

# open and read file
lines = open(INPUT).read().splitlines()

claims = {}
for line in lines:
    split_line = line.split('@')
    id = split_line[0].replace('#', '').strip()
    # split dimensions from starting points
    starting_dimensions = split_line[1].split(':')[0].split(',')
    dimensions = split_line[1].split(':')[1].split('x')
    starting_x = int(starting_dimensions[0].strip())
    starting_y = int(starting_dimensions[1].strip())
    x_length = int(dimensions[0].strip())
    y_length = int(dimensions[1].strip())
    for x in range(starting_x, starting_x + x_length):
        for y in range(starting_y, starting_y + y_length):
            claimed = x,y
            if  claims.get(claimed) is not None:
                claims[claimed].append(id)
            else:
                claims[claimed] = [id]

id_dicts = {}
for key, value in claims.iteritems():
    for v in value:
        alone = len(value) - 1
        id_dicts[v] = id_dicts.get(v, 0) + alone

for x, y in id_dicts.iteritems():
    if y == 0:
        print(x,y)
