#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    done=False
    f=""
    phrase="hackerrank"
    i=0
    # your code goes here
    for x in range (0, len(s)):
        if s[x:x+1]==phrase[i:i+1]:
            f+=phrase[i:i+1]
            i+=1
        if phrase==f:
            done=True
            print("YES")
            break
    if done== False:
        print("NO")