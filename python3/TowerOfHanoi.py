#!/usr/bin/env python3
import sys

def hanoi(start, temp, end, height):
    if height>0:
        #Move the top height-1 disks to the temp stack
        step1 = hanoi(start, end, temp, height-1)
        #Move the bottom disk to the end
        step2 = start+' '+end+'\n'
        #Move the height-1 disks from temp to the end
        step3 = hanoi(temp, start, end, height-1)
        return step1+step2+step3
    else:
        #Base case (height=0): return no text
        return '';

#argv[0] is always the program name
if len(sys.argv)==2:
    #Python starts indexing at 0
    height = int(sys.argv[1])
    if height<=8:
        print(hanoi('1','2','3',height))
