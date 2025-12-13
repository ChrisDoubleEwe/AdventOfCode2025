import math
import copy

filename = '09_in.txt';

max_x = 0
max_y = 0
parta = 0;

red = []
xs = []
ys = []

xs.append(0)
ys.append(0)

print("Reading input");
with open(filename) as f:
  for l in f:
    line = l.strip()
    coords = line.split(',');
    int_coords = []
    for c in coords:
      int_coords.append(int(c))
    if int_coords[0] > max_x:
      max_x = int_coords[0];
    if int_coords[1] > max_y:
      max_y = int_coords[1];
    xs.append(int_coords[0]);
    ys.append(int_coords[1]);

    red.append(int_coords)

red.append(red[0])
newxs = sorted(set(xs))
newys = sorted(set(ys))
xs = newxs
ys = newys

print(xs)
new_red = []

max_x = len(xs)
max_y = len(ys)

combos = len(red) * len(red);

map = []
row = []
print("Build map");
for i in range(0, max_x+1):
  row.append('.');
for i in range(0, max_y+1):
  map.append(copy.deepcopy(row));

print("Draw points");
last = []
for i in red:
  print("Points: " + str(i) + " / " + str(len(red)))
  real_x = xs.index(i[0])
  real_y = ys.index(i[1])

  map[real_y][real_x] = 'X'
  if len(last) == 0:
    last = i
    continue
  last_x = xs.index(last[0])
  last_y = ys.index(last[1])

  if real_y == last_y:
    if real_x < last_x:
      for x in range(real_x, last_x):
        map[real_y][x] = '#'
    else:
      for x in range(last_x, real_x):
        map[real_y][x] = '#'
  else:
    if real_y < last_y:
      for y in range(real_y, last_y):
        map[y][real_x] = '#'
    else:
      for y in range(last_y, real_y):
        map[y][real_x] = '#'

  last = i


print("Flood filling...")
# flood fill
map[0][0] = ' '
#map[max_y-1][max_x-1] = ' '

doing = 1
while doing == 1:
  print("flood iteration")
  doing = 0
  for x in range(0, max_x+1):
    for y in range(0, max_y+1):
      if map[y][x] == '.':
        if y > 0:
          if map[y-1][x] == ' ':
            map[y][x] = ' '
            doing = 1
        if y < max_y:
          if map[y+1][x] == ' ':
            map[y][x] = ' ' 
            doing = 1
        if x > 0:
          if map[y][x-1] == ' ':
            map[y][x] = ' ' 
            doing = 1
        if x < max_y:
          if map[y][x+1] == ' ':
            map[y][x] = ' '
            doing = 1


print("Flood fill complete");


for m in map:
  for x in m:
    print(x, end='')
  print('')

max_area = 0
count = 0
total = len(red) * len(red)

for a_i in range(0, len(red)):
  for b_i in range(0, len(red)):
    count += 1
    print (str(count) + " / " + str(total))
    if a_i == b_i:
      continue
    a_x = red[a_i][0];
    a_y = red[a_i][1];
    a_real_x = xs.index(a_x)
    a_real_y = ys.index(a_y)


    b_x = red[b_i][0];
    b_y = red[b_i][1];
    b_real_x = xs.index(b_x)
    b_real_y = ys.index(b_y)



    if a_real_x < b_real_x:
      lo_x = a_real_x
      hi_x = b_real_x
    else:
      lo_x = b_real_x
      hi_x = a_real_x
    if a_real_y < b_real_y:
      lo_y = a_real_y
      hi_y = b_real_y
    else:
      lo_y = b_real_y
      hi_y = a_real_y

    all_red = 1
    #print("Trying " + str(a_x) + "," + str(a_y) + " - " + str(b_x) + "," + str(b_y) + "...")
    for x in range(lo_x, hi_x+1):
      if all_red == 0:
        break
      for y in range(lo_y, hi_y+1):
        #print('-----');
        #print(x)
        #print(xs)
        #print(y)
        #print(ys)
        if map[y][x] == ' ':
          #print("Failed because " + str(x) + "," + str(y) + " is empty")
          all_red = 0
          break
        

    if all_red == 1:
      area = (abs(a_x-b_x)+1) * (abs(a_y-b_y)+1)
      if area > max_area:
        max_area = area

print("Part B: " + str(max_area))

