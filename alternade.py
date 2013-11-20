#!/usr/bin/env python

"""

An alternade is a word in which its letters, taken alternatively in a strict sequence, and used in the same order as the original word, make up at least two other words. All letters must be used, but the smaller words are not necessarily of the same length. For example, a word with seven letters where every second letter is used will produce a four-letter word and a three-letter word. Here are two examples:

  "board": makes "bad" and "or".
  "waists": makes "wit" and "ass".

Using the word list at http://www.puzzlers.org/pub/wordlists/unixdict.txt, write a program that goes through each word in the list and tries to make two smaller words using every second letter. The smaller words must also be members of the list. Print the words to the screen in the above fashion. 

"""
 
f = open("unixdict.txt")
for line in f:
    line = line.strip()
    length = len(line)
    word1 = ""
    word2 = ""
    for i in range(0, length,2):
        word1 +=line[i]
        try:
            word2 +=line[i+1]
        except:
            pass
    word1 = word1.strip()
    word2 = word2.strip()
    print line," ==> ", word1 ," and" , word2
