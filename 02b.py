filename = '02_in.txt';

partb = 0;
max_len = -1
min_len = 999999999


with open(filename) as f:
  for l in f:
    line = l.strip()
    rs = line.split(',');
    print(rs);

  for r in rs:
    invalids = 0
    print('   ');
    print(r);
    print('-------')
    ran = r.split('-');
    rlow=int(ran[0]);
    rhi = int(ran[1]);

    for i in range(rlow, rhi+1):
      if len(str(i)) < min_len:
        min_len = len(str(i))
      if len(str(i)) > max_len:
        max_len = len(str(i))

      this_num = list(str(i))
      this_len = len(str(i))
      # 1 : no repeats
      if this_len == 1:
        continue;

      # 2: digits must be equal
      if this_len == 2:
        if this_num[0] == this_num[1]:
          partb += i;
          print("Invalid ID: " + str(i));
          continue

      # 3: digits must be equal
      if this_len == 3:
        if this_num[0] == this_num[1] == this_num[2]:
          print("Invalid ID: " + str(i));
          partb += i;
          continue

      # 4: all equal or 2 pairs
      if this_len == 4:
        if this_num[0] == this_num[1] == this_num[2] == this_num[3]:
          partb += i;
          print("Invalid ID: " + str(i));
          continue
        if (this_num[0] == this_num[2]) and (this_num[1] == this_num[3]):
          partb += i;
          print("Invalid ID: " + str(i));
          continue
      # 5: all equal 
      if this_len == 5:
        if this_num[0] == this_num[1] == this_num[2] == this_num[3] == this_num[4]:
          partb += i;
          print("Invalid ID: " + str(i));
          continue
      # 6: all equal or 3x2 or 2x3
      if this_len == 6:
        if this_num[0] == this_num[1] == this_num[2] == this_num[3] == this_num[4] == this_num[5]:
          partb += i;
          print("Invalid ID: " + str(i));
          continue
        if (this_num[0] == this_num[3]) and (this_num[1] == this_num[4]) and (this_num[2] == this_num[5]):
          partb += i;
          print("Invalid ID: " + str(i));
          continue
        if (this_num[0] == this_num[2] == this_num[4]) and (this_num[1] == this_num[3] == this_num[5]):
          partb += i;
          print("Invalid ID: " + str(i));
          continue
      # 7: all equal 
      if this_len == 7:
        if this_num[0] == this_num[1] == this_num[2] == this_num[3] == this_num[4] == this_num[5] == this_num[6]:
          partb += i;
          print("Invalid ID: " + str(i));
          continue
      # 8: all equal or 4x2 or 2x4
      if this_len == 8:
        if this_num[0] == this_num[1] == this_num[2] == this_num[3] == this_num[4] == this_num[5] == this_num[6] == this_num[7]:
          partb += i;
          print("Invalid ID: " + str(i));
          continue
        if (this_num[0] == this_num[4]) and (this_num[1] == this_num[5]) and (this_num[2] == this_num[6]) and (this_num[3] == this_num[7]):
          partb += i;
          print("Invalid ID: " + str(i));
          continue;
        if (this_num[0] == this_num[2] == this_num[4] == this_num[6]) and (this_num[1] == this_num[3] == this_num[5] == this_num[7]):
          partb += i;
          print("Invalid ID: " + str(i));
          continue
      # 9: all equal or 3x3
      if this_len == 9:
        if this_num[0] == this_num[1] == this_num[2] == this_num[3] == this_num[4] == this_num[5] == this_num[6] == this_num[7] == this_num[8]:
          partb += i;
          print("Invalid ID: " + str(i));
          continue
        if (this_num[0] == this_num[3] == this_num[6]) and (this_num[1] == this_num[4] == this_num[7]) and (this_num[2] == this_num[5] == this_num[8]):
          partb += i;
          print("Invalid ID: " + str(i));
          continue
      # 10: all equal or 5x2 or 2x5
      if this_len == 10:
        if this_num[0] == this_num[1] == this_num[2] == this_num[3] == this_num[4] == this_num[5] == this_num[6] == this_num[7] == this_num[8] == this_num[9]:
          partb += i;
          print("Invalid ID: " + str(i));
          continue
        if (this_num[0] == this_num[5]) and (this_num[1] == this_num[6]) and (this_num[2] == this_num[7]) and (this_num[3] == this_num[8]) and (this_num[4] == this_num[9]):
          partb += i;
          print("Invalid ID: " + str(i));
          continue
        if (this_num[0] == this_num[2] == this_num[4] == this_num[6] == this_num[8]) and (this_num[1] == this_num[3] == this_num[5] == this_num[7] == this_num[9]):
          partb += i;
          print("Invalid ID: " + str(i));
          continue






          

  print("Min len: " + str(min_len))
  print("Max len: " + str(max_len))



print("Part B: " + str(partb));

