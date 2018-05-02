# Lab 5
# By Michelle Cantin

# Imports
import math
import sense_hat
s = sense_hat.SenseHat()

# Alphatical grade
def calcAlphaGrade(numGrade):
    # A+
    if (numGrade >= 90 and numGrade <= 100) :
        agrade = 'A+'
    # A
    elif (numGrade >= 85 and numGrade < 90):
        agrade = 'A'
    # A-
    elif (numGrade >= 80 and numGrade < 85):
        agrade = 'A-'
    # B+
    elif (numGrade >= 77 and numGrade < 80):
        agrade = 'B+'
    # B
    elif (numGrade >= 73 and numGrade < 77):
        agrade = 'B'
    # B-
    elif (numGrade >= 70 and numGrade < 73):
        agrade = 'B-'
    # C+
    elif (numGrade >= 67 and numGrade < 70):
        agrade = 'C+'
    # C
    elif (numGrade >= 63 and numGrade < 67):
        agrade = 'C'
    # C-
    elif (numGrade >= 60 and numGrade < 63):
        agrade = 'C-'
    # D+
    elif (numGrade >= 57 and numGrade < 60):
        agrade = 'D+'
    # D
    elif (numGrade >= 53 and numGrade < 57):
        agrade = 'D'
    # D-
    elif (numGrade >= 50 and numGrade < 53):
        agrade = 'D-'
    # F
    else:
        agrade = 'F'
    return agrade

# Numerical grade
def calcNumGrade(assPond, midPond, finPond, assMark, midMark, finMark):
    numGrade = round((( assMark / 100 ) * assPond) + (( midMark / 100 ) * midPond) + (( finMark / 100 ) * finPond),2)
    return (numGrade)

# Prompts
# Ponderation
# Assignments
assPond = float(input("What is the ponderation of assignments? "))
# Mid term
midPond = float(input("What is the ponderation of the mid term? "))
# Final
finPond = float(input("What is the ponderation of the final? "))
# Student mark
# Assignments
assMark = float(input("What mark did you get for your assignments? "))
# Mid term
midMark = float(input("What mark did you get for your mid term? "))
# Final
finMark = float(input("What mark did you get for your final? "))

# Numerical grade function call
numGrade = calcNumGrade(assPond, midPond, finPond, assMark, midMark, finMark)

# Alphatical grade function call
agrade = calcAlphaGrade(numGrade)

# Pass
if (numGrade >= 50):
    # Displays on console
    print("Congratulations, you passed with " + agrade)
    # Displays on Sense Hat
    s.show_message(agrade + " Congratulations, you passed!")
# Fail
else:
    # Displays on console
    print("You did not pass with " + agrade)
    # Displays on Sense Hat
    s.show_message(agrade + " You did not pass!")
