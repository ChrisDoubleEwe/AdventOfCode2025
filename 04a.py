filename = '04_in.txt';

parta = 0;

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

for y in range(0, rows+1):
  for x in range(0, cols+1):
    print(map[y][x], end ="")
  print('')

print('========');

for y in range(0, rows+1):
  for x in range(0, cols+1):
    if map[y][x] == '@':
      c = count(x,y);
      if c < 4:
        parta += 1

print("Part A: " + str(parta))

