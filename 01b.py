filename = '01_in.txt';

dial = 50
partb = 0;

print("- The dial starts by pointing at 50.");

with open(filename) as f:
  for l in f:
    line = l.strip()
    dir = line[0]
    val = int(line[1:])

    zeros = 0
    step = 0;
    if dir == 'R':
      step = 1
    else:
      step = -1

    for i in range(0, val):
      dial += step

      if dial > 99:
        dial -= 100

      if dial < 0:
        dial += 100

      if dial == 0:
        zeros += 1
        partb += 1

    print("- The dial is rotated by " + dir + str(val) + " to point at " + str(dial));
    print("    zeros: " + str(zeros));


print("Part B: " + str(partb))


