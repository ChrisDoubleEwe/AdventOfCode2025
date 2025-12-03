filename = '03_in.txt';

parta = 0;


with open(filename) as f:
  for l in f:
    line = l.strip()
    nums = list(line);
    print(nums);
    digit1_pos = -1
    digit1_val = -1

    digit2_pos = -1
    digit2_val = -1

    for i in range(0, len(nums)-1):
      if nums[i] > digit1_val:
        digit1_val = nums[i]
        digit1_pos = i

    for i in range(digit1_pos+1, len(nums)):
      if nums[i] > digit2_val:
        digit2_val = nums[i]
        digit2_pos = i

    final_val = int(str(digit1_val)+str(digit2_val))
    print(final_val)
    parta += final_val

print("Part A: " + str(parta))


