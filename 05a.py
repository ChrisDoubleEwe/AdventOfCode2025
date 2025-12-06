filename = '05_in.txt';

parta = 0;

fresh = [];
ing = []

doing_fresh = 1
with open(filename) as f:
  for l in f:
    line = l.strip()
    if line == '':
      doing_fresh = 0;
      continue
    if doing_fresh == 1:
      pair = line.split('-');
      int_pair = []
      int_pair.append(int(pair[0]))
      int_pair.append(int(pair[1]))
      fresh.append(int_pair)
    else:
      ing.append(int(line))

for i in ing:
  is_fresh = 0
  for p in fresh:
    if i >= p[0] and i <= p[1]:
      is_fresh = 1
  if is_fresh == 1:
    parta += 1

print("Part A: " + str(parta));

