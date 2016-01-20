Samples
=======

A set of example programs and build/execute scripts for different languages. Programs written in different languages will work the same. These programs are meant to demonstrate basic funtionality for reference.

Each language should be in its own folder. This folder should include source and resources for all examples.  It should contain a file named `run` which contains the commands for running the examples, and a file named `makefile`, which should be a build script. A build script is not required for languages that are not typically compiled.  Comments in the run file should be commented with #, such that they execute in bash (this is for clarity; run files should not be designed specifically for execution).


HelloWorld
----------

This is a very basic program that is mostly used to check the computer's ability to run programs in a given language.  If a computer cannot run HelloWorld, then check for a missing compiler/interpreter, an incorrect system PATH, file permissions, or something similar.

Provides the following output:

    Hello World


TowerOfHanoi
------------

This is a classic recursive program, and demonstrates input arguments, function declarations, and simple variable manipulation.

Shows the steps to solve a (Tower Of Hanoi)[https://en.wikipedia.org/wiki/Tower_of_Hanoi] with height<=8. The height of the tower is given as an argument. Each move is written on a new line, and shows the source pillar and destination pillar separated by a space.  The tower starts on pillar "1", ends on pillar "3", and uses pillar "2" as a placeholder.

Provides the following output (when height=3):

    1 3
    1 2
    3 2
    1 3
    2 1
    2 3
    1 3


SortFile
--------

Demonstrates built in functions for reading files, writing files, lists, and sorting, as well as string manipulation.

Sorts the contents of a textfile containing numbered lines. Throws an error if a line does not start with a number.  Input file provided with the command line interface after the prompt "Input:"

Given the following input file (unsorted.txt):

    3 A
    0 B
    1 C
    4 D
    5 E
    6 F
    9 G
    2 H
    7 I
    8 J

Provides the following output:

    Input:unsorted.txt

And the following output file (sorted.txt):

    0 B
    1 C
    2 H
    3 A
    4 D
    5 E
    6 F
    7 I
    8 J
    9 G



TODO:
 * Be thorough, but brief
 * Do this in C
 * Do this in Java
 * Something with random numbers
 * Something with third party libraries
 * Something with Structures