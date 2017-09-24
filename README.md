# Reviz
Python script to enable the use of text files as revision quizzes.

## What is this script for?
This script takes an input file (plain text file; no fancy formats) with questions specified in a simple format and tests the user with the questions. It supports auto-grading and self-grading.

Currently, only Fill-in-the-blank and Multiple-Choice Questions have been tested, but probably many other styles of questions can work :)

## Preparing an Input File
Questions can be specified in the following format:
`<answer> |:| <question>`

If it is a Multiple-Choice Question, it can be formatted this way:
`<answer> |:| <question> |:| <choices>`
(Note: "|:|" may not be necessary. Refer to the following section.)

### Details of each field
(example sourced from: https://en.wikipedia.org/wiki/DNA)

**1. Answer Field**

Type the exact answer. Do note that auto-grader is case-sensitive.
e.g. `nucleic acids`

**2. Question Field**

`{}` can be used to denote where a blank should be placed, e.g.
`DNA and ribonucleic acid (RNA) are {}; alongside proteins, lipids and complex carbohydrates (polysaccharides), they are one of the four major types of macromolecules that are essential for all known forms of life.`

**3. Choices Field**

There are 2 ways in which choices can be formatted. For short choices, a simple way is to do the following:
|:| <choice 1> :: <choice 2> :: <choice 3>

For longer choices, they can each be specified on a line.
There is no limit on number of choices you may specify, although the auto-labelling will not work after 26 choices.

### Complete Example
**1. Fill-in-the-blank**
```
nucleic acids |:| DNA and ribonucleic acid (RNA) are {}; alongside proteins, lipids and complex carbohydrates (polysaccharides), they are one of the four major types of macromolecules that are essential for all known forms of life.
```

will display as:
```
DNA and ribonucleic acid (RNA) are _____________; alongside proteins, lipids and complex carbohydrates (polysaccharides), they are one of the four major types of macromolecules that are essential for all known forms of life.
```

**2. MCQ**
```
A |:| DNA and ribonucleic acid (RNA) are {}; alongside proteins, lipids and complex carbohydrates (polysaccharides), they are one of the four major types of macromolecules that are essential for all known forms of life. |:| nucleic acids :: nucleobases :: amino acids :: nucleotides
```
or
```
A |:| DNA and ribonucleic acid (RNA) are {}; alongside proteins, lipids and complex carbohydrates (polysaccharides), they are one of the four major types of macromolecules that are essential for all known forms of life.
nucleic acids
nucleobases
amino acids
nucleotides
```

will both display as:
```
DNA and ribonucleic acid (RNA) are _____________; alongside proteins, lipids and complex carbohydrates (polysaccharides), they are one of the four major types of macromolecules that are essential for all known forms of life.
A: nucleic acids
B: nucleobases
C: amino acids
D: nucleotides
```
