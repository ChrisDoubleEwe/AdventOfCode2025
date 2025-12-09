import math

filename = '08_in.txt';

parta = 0;

boxes = []
seen = []
circuits = []

with open(filename) as f:
  for l in f:
    line = l.strip()
    coords = line.split(',');
    int_coords = []
    for c in coords:
      int_coords.append(int(c))
    boxes.append(int_coords)
   

def not_yet_seen(a,b):
  global seen
  keya = str(a[0])+'.'+str(a[1])+'.'+str(a[2])
  keyb = str(b[0])+'.'+str(b[1])+'.'+str(b[2])
  key = keya+':'+keyb
  if key in seen:
    return False
  else:
    return True

def dist(a, b):
  s0 = (a[0]-b[0]) * (a[0]-b[0])
  s1 = (a[1]-b[1]) * (a[1]-b[1])
  s2 = (a[2]-b[2]) * (a[2]-b[2])

  res = math.sqrt(s0+s1+s2)
  return(res)

for i in range(0, 1000):
  print(i)
  closest = 9999999999999999;
  closest_pair = []

  #print(seen)
  for a in boxes:
    for b in boxes:
      if a == b:
        continue
      this_dist = dist(a, b)
      if this_dist < closest and not_yet_seen(a,b):
        closest = this_dist;
        closest_pair = [];
        closest_pair.append(a);
        closest_pair.append(b);

  #print('==========')
  #print(closest_pair)
  #print(closest)
  a = closest_pair[0]
  b = closest_pair[1]
  keya = str(a[0])+'.'+str(a[1])+'.'+str(a[2])
  keyb = str(b[0])+'.'+str(b[1])+'.'+str(b[2])
  seen.append(keya+":"+keyb)
  seen.append(keyb+":"+keya)

  added = 0
  for c in range(0, len(circuits)):
    # Both already in a circuit
    if a in circuits[c] and b in circuits[c]:
      added = 1;
      break
    # a already in a circuit
    if a in circuits[c] and b not in circuits[c]:
      merge = -1
      for d in range(0, len(circuits)):
        if b in circuits[d]:
          merge = d
      circuits[c].append(b)
      if merge > -1:
        for x in circuits[merge]:
          if x not in circuits[c]:
            circuits[c].append(x)
        circuits.pop(merge)
      added = 1;
      break;
    if b in circuits[c] and a not in circuits[c]:
      merge = -1
      for d in range(0, len(circuits)):
        if a in circuits[d]:
          merge = d
      circuits[c].append(a)
      if merge > -1:
        for x in circuits[merge]:
          if x not in circuits[c]:
            circuits[c].append(x)
        circuits.pop(merge)
      added = 1;
      break;
  # Neither already in a circuit
  if added == 0:
    pair = [];
    pair.append(a)
    pair.append(b)
    circuits.append(pair);
  
  #print("-CIRCUITS-----------------------");
  #for c in circuits:
  #  print(c)
  #print("--------------------------------");


lengths=[]
for c in circuits:
  lengths.append(len(c));

lengths_sorted = sorted(lengths)
lengths_sorted.reverse()
print(lengths_sorted)

parta = lengths_sorted[0] * lengths_sorted[1] * lengths_sorted[2] 

print("Part A: " + str(parta))




