#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    c = chr(i)
    if i % 2 != 0:
        c = chr(i - 32)
    print("{}".format(c), end="")
