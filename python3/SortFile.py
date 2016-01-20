#!/usr/bin/env python3
import sys
import traceback

#Prompt user for input file
InputFileName = input('Input:')
#Create an empty list of numbered lines
NumberedLines = []

#Open file for reading
#You can also use InputFile = open(InputFileName),
#but in python, the with-as statement 
#assures the file is closed
with open(InputFileName) as InputFile:
    #Put lines into a list for sorting
    for line in InputFile:
        #Splits line at spaces.  The 1 means only the first
        #split is done (the rest is left together as element[1])
        index = line.split(' ',1)[0]
        try:
            #Gets the first word as a number
            index = float(index)
            #Add a tuple with the index and line text to NumberedLines
            NumberedLines.append((index,line))
        except ValueError:
            #If the first word turned out not to be a number, error
            traceback.print_exc(file=sys.stdout)
            print('Error Parsing '+InputFileName+': '+
                  str(index)+' is not a float')
            print('While Parsing>>'+line)
            sys.exit(1)

NumberedLines.sort()

#Open the output file with the writing option ('w').
#'a' appends, 'r+' reads and writes, and 'r' only reads (default)
with open('sorted.txt','w') as OutputFile:
    for line in NumberedLines:
        OutputFile.write(line[1])
