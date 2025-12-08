filename = '07_in.txt';

parta = 0;

map = []

with open(filename) as f:
  for l in f:
    line = l.strip()
    line = line.replace('S','|');
    row = []
    for l in line:
      row.append(l)
    map.append(row)

for row in range(1, len(map)):
  for col in range(0, len(map[0])):
    if map[row][col] == '.' and map[row-1][col] == '|':
      map[row][col]  = '|'
      continue
    if map[row][col] == '^' and map[row-1][col] == '|':
      map[row][col-1]  = '|'
      map[row][col+1]  = '|'
      parta += 1
      continue
  #print(map[row])

print("Part A: " + str(parta))

