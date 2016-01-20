#!/usr/bin/env python3
import sys
import traceback

#Prompt user for input file
InputFileName = input('Input:')
#Open file for reading
InputFIle = open(InputFileName)
#Create an empty list of numbered lines
NumberedLines = []

#Put lines into a list for sorting
for line in InputFile:
    index = ' '.split(line)[0]
    try:
        index = float(index)
    except ValueError:
        traceback.print_exc(file=sys.stdout)
        print('Error Parsing '+InputFile+': '+index+' is not a float')
        print('While Parsing>>'+line)
        sys.exit(1)
    #Add a tuple with the index and line text to NumberedLines
    NumberedLines.append((index,line))

NumberedLines.sort()

#Open the output file with the writing option ('w').
#'a' appends, 'r+' reads and writes, and 'r' only reads (default)
OutputFile = open('sorted.txt','w')

for line in OutputFile:
    
