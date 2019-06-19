#!python3
import os
import time
import random
from sys import platform

print("Welcome to Reviz! Please ensure that input file is formatted properly, \n\t(refer to README.md & exampleInput.txt)\n\n")
test_file = input("ENTER FILE NAME OR PATH: ")
test_mode = int(input("ENTER MODE ([1] AUTO-GRADING | [2] SELF-GRADING): "))
#test_file = "test.txt"
#test_mode = 1

fin = open(test_file, "r")
questions = []
instructions = ""

total = 0
correct = 0
blankLength = 0

wrong = []

isInstructions = True;
thisQuestion = ""
sect = 0

for line in fin:
    #Check if potentially reading instructions from file
    if isInstructions:
        instructions += line

        #check for a line with hyphens
        if line == '-'*(len(line)-1)+'\n' and len(line) > 1:
            #End of instruction, subsequent data is the real deal
            isInstructions = False

            #instruction is present in this file,
            #so anything that is added should be undone.
            blankLength = 0
            total = 0
            thisQuestion = ""
            sect = 0
            questions = []
            continue;
    
    #Read in questions from file
    if line == "\n":
        questions.append(thisQuestion)
        thisQuestion = ""
        total += 1
    else:
        token = line.split('|:|')
        if thisQuestion == "":
            blankLength = max(blankLength, len(token[0]))
            sect = len(token)
        else:
            if sect <= 2:
                thisQuestion += " |:| "
            else:
                thisQuestion += " :: "
            sect += 1
        thisQuestion += line.strip("\n")

if isInstructions:
    #there was never a line separating the instruction and questions,
    #thus the recorded string is likely just the questions.
    instructions = ""

if thisQuestion != "":
    questions.append(thisQuestion)
    thisQuestion = ""
    total += 1



if platform == "win32":
    os.system("cls")
else:
    os.system("clear")



while questions:
    random.seed = (os.urandom(1024))
    line = random.choice(questions)
    questions.remove(line)
    qn = line.split('|:|')

    if len(qn) < 2:
        #parsing error may have occured. skipping.
        total -= 1
        continue

    print(instructions)
    print(qn[1].strip().format("_"*blankLength))
    if len(qn) > 2:
        label = 'A'
        for option in qn[2].strip().split("::"):
            print("{}: {}".format(label, option.strip()))
            label = chr(ord(label)+1)
    print()
    
    if (test_mode == 1):
        usr = input()
        usr = usr.strip()
        if (usr.lower() == qn[0].strip().lower()):
            print("Correct!")
            correct += 1
        else:
            print("Incorrect :/")
            print("The answer is", qn[0])
            wrong.append((line, usr))
    else:
        input("Press enter to show answer...\n")
        print(qn[0].strip())
        usr = input("\nDid you get it correct? [Y/N]> ")
        if (usr.upper() == 'Y'):
            print(":D")
            correct += 1
        elif (usr.upper() == 'N'):
            print(":/")
            wrong.append(line)
    
    time.sleep(1)
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

print("You got " + str(correct) + " correct out of " + str(total) + ".\n")

time.sleep(1)

if correct != total:
    print("Here are the ones you got wrong:\n")
    if (test_mode == 1):
        for a, b in wrong:
            qn = a.split(' |:| ')
            print(qn[1].format("_"*blankLength))
            if len(qn) > 2:
                label = 'A'
                for option in qn[2].split(" :: "):
                    print("{}: {}".format(label, option))
                    label = chr(ord(label)+1)
            print("Answer:", qn[0])
            print("Your answer:", b)
            print()
    else:
        for a in wrong:
            qn = a.split(' |:| ')
            print(qn[1].format("_"*blankLength))
            if len(qn) > 2:
                label = 'A'
                for option in qn[2].split(" :: "):
                    print("{}: {}".format(label, option))
                    label = chr(ord(label)+1)
            print("Answer:", qn[0])
            print()
    time.sleep(1)
        
