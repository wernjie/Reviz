#!python3
import os
import random

print("Welcome to Reviz! Please ensure that input file is formatted properly, \n\t(refer to README.md)\n\n")
test_file = input("ENTER FULL\RELATIVE FILE NAME OR PATH: ")
test_mode = int(input("ENTER MODE ([1] AUTO-GRADING | [2] SELF-GRADING): "))
#test_file = "test.txt"
#test_mode = 1

os.system("cls")

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
        if isInstructions:
                instructions += line
                if line == '-'*(len(line)-1)+'\n':
                        isInstructions = False
        else:
                if line == "\n":
                        questions.append(thisQuestion)
                        thisQuestion = ""
                        total += 1
                else:
                        token = line.split(' |:| ')
                        if thisQuestion == "":
                                blankLength = max(blankLength, len(token[0]))
                                sect = len(token)
                        else:
                                if sect <= 2:
                                        thisQuestion += " |:| "
                                else:
                                        thisQuestion += " :: "
                                sect += 1
                        thisQuestion += line.strip(" \n")
if thisQuestion != "":
        questions.append(thisQuestion)
        thisQuestion = ""
        total += 1

while questions:
        random.seed = (os.urandom(1024))
        line = random.choice(questions)
        questions.remove(line)
        qn = line.split(' |:| ')
        print(instructions)
        print(qn[1].format("_"*blankLength))
        if len(qn) > 2:
                label = 'A'
                for option in qn[2].split(" :: "):
                        print("{}: {}".format(label, option))
                        label = chr(ord(label)+1)
        print()
        
        if (test_mode == 1):
                usr = input()
                usr = usr.strip(" \n")
                if (usr == qn[0]):
                        print("Correct!")
                        correct += 1
                else:
                        print("Incorrect :/")
                        print("The answer is", qn[0])
                        wrong.append((line, usr))
        else:
                input("Press enter to show answer...\n")
                print(qn[0])
                usr = input("\nDid you get it correct? [Y/N]> ")
                if (usr.upper() == 'Y'):
                        print(":D")
                        correct += 1
                elif (usr.upper() == 'N'):
                        print(":/")
                        wrong.append(line)
       
        os.system("Pause")
        os.system("cls")

print("You got", correct, "correct out of", total, ".\n")
os.system("Pause")
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
        os.system("Pause")
                
