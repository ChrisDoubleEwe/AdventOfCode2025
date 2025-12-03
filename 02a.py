filename = '02_in.txt';

parta = 0;


with open(filename) as f:
  for l in f:
    line = l.strip()
    rs = line.split(',');
    print(rs);

  for r in rs:
    invalids = 0
    print('   ');
    print(r);
    ran = r.split('-');
    rlow=int(ran[0]);
    rhi = int(ran[1]);
    len_low = len(str(rlow))/2;
    if len_low == 0:
      len_low = 1
    start = int(str(rlow)[0:len_low])

    brk = 0
    while brk == 0:
      this_num = int(str(start)+str(start));
      if this_num >= rlow and this_num <= rhi:
        invalids += 1
        parta += this_num;
        print(" INVALID: " + str(this_num));

      if this_num > rhi:
        brk = 1

      start += 1
   
print('----------')
print("Part A: " + str(parta))


