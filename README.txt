				CSC 120 - Project 1
Author : Sparsh Goyal
Date : Jan 27, 2019

This project is being developed using PyCharm 2018.2.3

**To Compile and run the source code in Command prompt or Terminal following should be carefully checked:
  --> python dfa.py dfa.txt strings.txt answers.txt
     ##All the parameters like, dfa.txt strings.txt and answers.txt, to be passed with the source code ( dfa.py ) should be placed in the same folder otherwise appropriate location of the parameter should be passed.

It should generate following output according to the input files :

*****************************************************************************************
Sparshs-MacBook-Pro:documents sparshgoyal$ python DFA.py dfa.txt strings.txt answers.txt
___________________________DFA_____________________________
baaab
Alphabets are:
a
b
('Total number of states:', '3')
('Initial state:', '1')
accepting states are:
1
2
('Number of lines in dfa.txt are :', 11)
['baaab\n', 'aab\n', 'ababa\n', 'baba']
['1', 'a', '2']
['1', 'b', '3']
['2', 'a', '2']
['2', 'b', '2']
['3', 'a', '3']
['3', 'b', '3']
6
Sparshs-MacBook-Pro:documents sparshgoyal$
*****************************************************************************************

**To open answers.txt in Mac OS terminal:
--> Sparshs-MacBook-Pro:documents sparshgoyal$ open answers.txt
**To open answers.txt in Command Prompt :
--> answers.txt