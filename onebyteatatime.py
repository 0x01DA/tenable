#!/usr/bin/env python3

from pwn import *
from string import ascii_lowercase, printable, digits
import re

def test_flag(flag):
  ret = sh.recvuntil(b"\x00")
  print(ret.decode())
  print("Send '{}'".format(flag))
  sh.send(bytes("{}\n".format(flag), encoding='utf8'))
  sh.recvuntil("\r\n")
  ret = sh.recvuntil("\r\n")
  print(ret.decode())
  if b"...Exiting" in ret:
    return -1
  chars = ret.decode().split("the first ")
  chars = chars[1].split(" ")[0]
  print(chars[0] + " ")
  ret = sh.recvuntil("IPv4 address I have...\r\n\r\n")
  print(ret.decode())
  xor_base = sh.recvuntil(delims="\r\n", drop=True)
  print(xor_base)
  return int(chars)




# context.log_level = 'debug'


flag = "flag{f0ll0w_th3_whit3_r@"

for c in ascii_lowercase + digits + "}{@_":
  sh = remote('challenges.ctfd.io',30468)
  found = test_flag(flag + c)
  if found > 0:
    flag = flag + c
    print("\n\nFound {} for position: {}\n\n".format(c, found))

#m = re.findall(r'(0.*\d+).*',ret.decode())
#print(m[0])

sh.close()
