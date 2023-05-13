import math
import random
import time

weight = 1 #[0]
weightPrev = 0  #[0]
error = 0
errorPrev = 0
inputCodes = [-1, 1]
bestError = 0
bestWeigth =0
bestEpoc = 0

#print("Init weight is " + str(weight))

for i in range(200):
    print(">  BEGIN EPOC "+str(i+1))
    print("Current EPOC Weight: " + str(weight))

    inputChosen = random.randint(0, 1)
    #inputChosen = 0
    print("Select signal value " + str(inputCodes[inputChosen]))

    answer = inputCodes[inputChosen] * weight
    print("Answer: " + str(answer))

    error = abs(inputCodes[inputChosen] - answer)

    if error > errorPrev:
        print("Current Error: " + str(error))
        print("Previous Error : " + str(errorPrev))
        print("DECISION: Current error more than previous so save previous weight")
        weight = weightPrev
    else:
        print("Current Error: " + str(error))
        print("Previous Error : " + str(errorPrev))
        print("DECISION: Current error less than previous error. This experiment more accurate. Save current results as best")
        errorPrev = error
        weightPrev = weight

        bestError = error
        bestWeigth = weight
        bestEpoc = i+1

    weight += random.randint(-1, 1)/100 #delta

    print("Best error is "+ str(bestError))
    print("Best weight is " + str(bestWeigth))
    print("Best EPOC  is " + str(bestEpoc))
    print("Answer predict is " + str(answer))
    print("New  EPOC Weight: " + str(weight))
