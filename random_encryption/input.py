#!/usr/bin/env python3

import random

rands = [
[249, 182, 79],
[136, 198, 95],
[159, 167, 6],
[223, 136, 101],
[66, 27, 77],
[213, 234, 239],
[25, 36, 53],
[89, 113, 149],
[65, 127, 119],
[50, 63, 147],
[204, 189, 228],
[228, 229, 4],
[64, 12, 191],
[65, 176, 96],
[185, 52, 207],
[37, 24, 110],
[62, 213, 244],
[141, 59, 81],
[166, 50, 189],
[228, 5, 16],
[59, 42, 251],
[180, 239, 144],
[13, 209, 132],
]
res = [184, 161, 235, 97, 140, 111, 84, 182, 162, 135, 76, 10, 69, 246, 195, 152, 133, 88, 229, 104, 111, 22, 39]



def encrypt(flag: str):
  seeds = []
  for i in range(0,len(flag)):
      seeds.append(random.randint(0,10000))

  res = []
  for i in range(0, len(flag)):
      random.seed(seeds[i])
      rands = []
      for j in range(0,4):
          rands.append(random.randint(0,255))

      res.append(ord(flag[i]) ^ rands[i%4])
      del rands[i%4]
      print("RANDS: " + str(rands))

  print("RES: {}".format(res))
  print("SEEDS: {}".format(seeds))

  return res, seeds


def find_seed(rands, res):
  result = {}
  for i in range(10000):
    random.seed(i)
    trands = []
    for k in range(0,4):
      trands.append(random.randint(0,255))

    for ri in range(0,len(res)):
      tmp_list = trands.copy()
      missing = tmp_list.pop(ri%4)
      if rands[ri] == tmp_list:
        # print("Position: {} Seed: {} rand: {} missing: {}".format(ri, i, rands[ri], missing))
        result[ri] = missing
        # print(chr(res[ri] ^ missing))

  return result


#encrypt(flag)

flag = ""

found_seeds = find_seed(rands, res)
for k, v in sorted(found_seeds.items()):
  flag = flag + chr(res[k] ^ v)

print(flag)

