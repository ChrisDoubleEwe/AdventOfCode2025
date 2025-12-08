filename = '07_in.txt';

partb = 0;

map = []
num = []

with open(filename) as f:
  for l in f:
    line = l.strip()
    row = []
    num_row = []
    for l in line:
      row.append(l)
      num_row.append(0)
    map.append(row)
    num.append(num_row)



for row in range(0, len(map)):
  for col in range(0, len(map[0])):
    if map[row][col]=='S':
      num[row][col]=1
      continue
    if row > 0:
      if map[row][col] == '.':
        num[row][col] += num[row-1][col] 
      if map[row][col] == '^':
        num[row][col-1] += num[row-1][col]
        num[row][col+1] += num[row-1][col]


result = 0
for n in num[len(num)-1]:
  result += n

print("Part B: " + str(result))

