filename = '06_in.txt';

partb = 0;

grid = []

with open(filename) as f:
  for l in f:
    line = l[:-1]
    grid.append(line)


transposed = []
for col in range(0, len(grid[0])):
  this_col = ''
  for row in range(0, len(grid)):
    this_col += grid[row][col]
  transposed.append(this_col)

transposed.append('  ');
    
op = ''
result = 0

for i in transposed:
  if i.strip() == '':
    partb += result
    continue

  if '*' in i or '+' in i:
    result = int(i[:-1])
    if '*' in i:
      op = '*'
    else:
      op = '+'
  else:
    if op == '+':
      result = result + int(i)
    else:
      result = result * int(i)

print("Part B: " + str(partb))
