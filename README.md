# list-to-staircase-structure-exercise

A Python function that takes in a list of integers and returns them rearranged into a staircase, if possible, or False otherwise. A staircase is a list of lists where list 0 has length 1, and every list i+1 is one item longer than list i. The order of the elements in the staircase doesn’t matter.

**Exercise** : Develop a function named decode(). This function should read an encoded message from a .txt file and return its decoded version as a string.

Your function must be able to process an input file with the following format:

    3 love
    6 coding
    2 dogs
    4 cats
    1 I
    5 you
    7 bdc

In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure. The pyramid increases by one number per line, like so:

      1
     2 3
    4 5 6

The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6). You should ignore all the other words. So for the example input file above, the message words are:

    1: I
    3: love
    6: coding
   
and your function should return the string "I love coding".

