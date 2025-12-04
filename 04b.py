import copy

filename = '04_in.txt';

partb = 0;

map = [];
rows = 0;
cols = 0;

with open(filename) as f:
  for l in f:
    rows += 1
    line = l.strip()
    row = list(line);
    map.append(row);
    cols = len(l)-2;

rows = rows-1

for r in map:
  print(r);

print(rows)
print(cols)

def count(x,y):
  total = 0
  if y > 0:
    if x > 0:
      if map[y-1][x-1] == '@':
        total += 1
    if x < cols:
      if map[y-1][x+1] == '@':
        total += 1
    if map[y-1][x] == '@':
      total += 1
  if y < rows:
    if x > 0:
      if map[y+1][x-1] == '@':
        total += 1
    if x < cols:
      if map[y+1][x+1] == '@':
        total += 1
    if map[y+1][x] == '@':
      total += 1
  if x > 0:
    if map[y][x-1] == '@':
      total += 1
  if x < cols:
    if map[y][x+1] == '@':
      total += 1

  return(total)

this_round_removed = 0;
finished = 0;

while finished == 0:
  this_round_removed = 0;

  new_map = copy.deepcopy(map);

  for y in range(0, rows+1):
    for x in range(0, cols+1):
      if map[y][x] == '@':
        c = count(x,y);
        if c < 4:
          partb += 1
          this_round_removed += 1
          new_map[y][x] = '.'

  map = copy.deepcopy(new_map);
  if this_round_removed == 0:
    finished = 1

print("Part B: " + str(partb))
