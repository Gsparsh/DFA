""""
Author = Sparsh Goyal
Date = Jan 27, 2019
CSC 212 - Project 1
Project Title : "Deterministic Finite Automation"
"""


import sys
with open(sys.argv[1], 'r') as f:             #reading dfa.txt
    dfa = f.readlines()
length = len(dfa)
with open(sys.argv[2], 'r') as t:             #reading strings.txt
    strings = t.readlines()


print("------------------------------------DFA----------------------------------")
alpha = []                          #initialize array
accept = []                          #initialize array
strn = []
alphabet = dfa[0].split()           #splitting dfa alphabets
nrstates = dfa[1].split()           #splitting dfa nrstates
initial = dfa[2].split()            #splitting initial state
accepting = dfa[3].split()          #splitting accepting states
transition = []
for x in strings:
    strn.append(x)



qinit = initial[1]

nstates= nrstates[1]
print("Alphabets are:")
for x in range(len(alphabet)-2):          ##displaying alphabets
    alpha.append(alphabet[x+2])
    print(alpha[x])

print(" Total number of states:",nstates)     #displaying number of states
print(" Initial state:",qinit)                #displaying initial states
print(" Accepting states are:")               #displaying accepting states
for x in range(len(accepting)-1):
    accept.append(accepting[x+1])
    print(accepting[x+1])


print(" Input Strings are: \n", strn)
print(" DFA transitions are:")
for x in range(length-5):
    transition.append(dfa[x+5].split())
    print(transition[x])


def function(trans,init,accepts,s):           #****MAIN FUNCTION****
    curr_state = init
    for c in s:
        for x in range(len(trans)):
            if curr_state == trans[x][0] and c == trans[x][1]:
                curr_state = trans[x][2]

    return curr_state in accepts
s = open(sys.argv[3], 'w+')             #writing answers.txt
s.write("--------DFA RESULTS------\n")
s.write("Result  Input String\n")
for i in range(len(strn)):
    if function( transition, qinit, accept, strn[i]) == True:
        s.write("   Yes   "+str(strn[i]))

    else:
        s.write(("   No   "+strn[i]))

s.close()



