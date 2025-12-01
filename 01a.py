filename = '01_in.txt';

dial = 50
parta = 0;

print("- The dial starts by pointing at 50.");

with open(filename) as f:
  for l in f:
    line = l.strip()
    dir = line[0]
    val = int(line[1:])

    if dir == 'R':
      dial += val
    else:
      dial -= val

    while dial > 99:
      if dial > 99:
        dial -= 100

    while dial < 0:
      if dial < 0:
        dial += 100

    if dial == 0:
      parta += 1

    print("- The dial is rotated by " + dir + str(val) + " to point at " + str(dial));


print("Part A: " + str(parta))


