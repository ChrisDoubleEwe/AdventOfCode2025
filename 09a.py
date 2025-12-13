import math

filename = '09_in.txt';

parta = 0;

red = []

with open(filename) as f:
  for l in f:
    line = l.strip()
    coords = line.split(',');
    int_coords = []
    for c in coords:
      int_coords.append(int(c))
    red.append(int_coords)

print(red)

max_area = 0
for a in red:
  for b in red:
    area = (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)
    if area > max_area:
      max_area = area

print("Part A: " + str(max_area))
  
