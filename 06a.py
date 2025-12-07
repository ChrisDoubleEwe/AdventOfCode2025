filename = '06_test.txt';

parta = 0;

grid = []

with open(filename) as f:
  for l in f:
    line = l.strip()
    lanes = line.split();
    grid.append(lanes)

for i in range(0, len(grid[0])):
  result = int(grid[0][i])
  for j in range(1, len(grid)-1):
    if grid[len(grid)-1][i] == "*":
      result = result * int(grid[j][i])
    else:
      result = result + int(grid[j][i])

  parta += result
    
print("Part A: " + str(parta))
    
