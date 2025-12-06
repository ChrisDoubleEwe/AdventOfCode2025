import copy

filename = '05_in.txt';

partb = 0;

fresh = [];
ing = []
boundaries = []

lowest = -1
highest = -1

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
      boundaries.append(int(pair[0]))
      boundaries.append(int(pair[1]))

    else:
      ing.append(int(line))

lowest = fresh[0][0]
highest = fresh[0][1]

bounds = sorted(set(boundaries))

merged = 0
doing = 1
while doing == 1:
  merged = 0
  for i in range(0, len(fresh)):
    if merged == 1:
      break
    for j in range(0, len(fresh)):
      if merged == 1:
        break
      if i == j:
        continue
      # remove duplicates
      if fresh[i][1] == fresh[j][1] and fresh[i][0] == fresh[j][0]:
        fresh.pop(j)
        merged = 1
        break;

      # 10-12 | 9-13 -> 9-13

      # 10-14 | 12-18 -> 10-18
      if fresh[i][1] >= fresh[j][0] and fresh[i][1] <= fresh[j][1]:
        if fresh[j][0] < fresh[i][0]:
          #fresh[j][1] = fresh[i][1];
          fresh.pop(i)
          merged = 1 
          break;
        else:
          fresh[i][1] = fresh[j][1];
          fresh.pop(j)
          merged = 1
          break;
      # 2-4 | 3-4 -> 2-4
          
  if merged == 0:
    doing = 0


f = sorted(fresh)
for i in range(0, len(f)):
  partb += f[i][1] - f[i][0] + 1

print("Part B: " + str(partb))
