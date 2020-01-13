aisles = {}
data = open('info.txt').read().splitlines()

aisle_designator = 0

for line in data:
    if line == '':
        aisle_designator += 1
    elif line == 'hbc':
        aisle_designator = 'hbc'
    elif line == 'front':
        aisle_designator = 'front'
    elif line == 'back':
        aisle_designator = 'back'
    elif line == 'pharmacy':
        aisle_designator = 'pharmacy'
    else:
        aisles[line.lower()] = 'aisle ' + str(aisle_designator)
aisles_full = aisles
