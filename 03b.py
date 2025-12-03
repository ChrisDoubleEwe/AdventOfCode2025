filename = '03_in.txt';

partb = 0;


with open(filename) as f:
  for l in f:
    line = l.strip()
    nums = list(line);
    print(nums);
    digit1_pos = -1
    digit1_val = -1

    digit2_pos = -1
    digit2_val = -1

    digit3_pos = -1
    digit3_val = -1

    digit4_pos = -1
    digit4_val = -1

    digit5_pos = -1
    digit5_val = -1

    digit6_pos = -1
    digit6_val = -1

    digit7_pos = -1
    digit7_val = -1

    digit8_pos = -1
    digit8_val = -1

    digit9_pos = -1
    digit9_val = -1

    digit10_pos = -1
    digit10_val = -1

    digit11_pos = -1
    digit11_val = -1

    digit12_pos = -1
    digit12_val = -1


    for i in range(0, len(nums)-11):
      if nums[i] > digit1_val:
        digit1_val = nums[i]
        digit1_pos = i

    for i in range(digit1_pos+1, len(nums)-10):
      if nums[i] > digit2_val:
        digit2_val = nums[i]
        digit2_pos = i

    for i in range(digit2_pos+1, len(nums)-9):
      if nums[i] > digit3_val:
        digit3_val = nums[i]
        digit3_pos = i

    for i in range(digit3_pos+1, len(nums)-8):
      if nums[i] > digit4_val:
        digit4_val = nums[i]
        digit4_pos = i

    for i in range(digit4_pos+1, len(nums)-7):
      if nums[i] > digit5_val:
        digit5_val = nums[i]
        digit5_pos = i

    for i in range(digit5_pos+1, len(nums)-6):
      if nums[i] > digit6_val:
        digit6_val = nums[i]
        digit6_pos = i

    for i in range(digit6_pos+1, len(nums)-5):
      if nums[i] > digit7_val:
        digit7_val = nums[i]
        digit7_pos = i

    for i in range(digit7_pos+1, len(nums)-4):
      if nums[i] > digit8_val:
        digit8_val = nums[i]
        digit8_pos = i

    for i in range(digit8_pos+1, len(nums)-3):
      if nums[i] > digit9_val:
        digit9_val = nums[i]
        digit9_pos = i

    for i in range(digit9_pos+1, len(nums)-2):
      if nums[i] > digit10_val:
        digit10_val = nums[i]
        digit10_pos = i

    for i in range(digit10_pos+1, len(nums)-1):
      if nums[i] > digit11_val:
        digit11_val = nums[i]
        digit11_pos = i

    for i in range(digit11_pos+1, len(nums)):
      if nums[i] > digit12_val:
        digit12_val = nums[i]
        digit12_pos = i



    final_val = int(str(digit1_val)+str(digit2_val)+str(digit3_val)+str(digit4_val)+str(digit5_val)+str(digit6_val)+str(digit7_val)+str(digit8_val)+str(digit9_val)+str(digit10_val)+str(digit11_val)+str(digit12_val))
    print(final_val)
    partb += final_val

print("Part B: " + str(partb))


