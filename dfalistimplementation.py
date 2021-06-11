#transition table for states: q0,q1,q2
states_trans = {
                    "q0":{0:"q1",1:"q0"},
                    "q1":{0:"q1",1:"q2"},
                    "q2":{0:"q1",1:"q0"}
                   }
#Everything is maintained in the list format
initialState = ["q0"]
finalState = ["q2"]
inputSymbols = ["0","1"]
path = []
currentState = []
def initializationDFA(inputString):
    inputString = inputString.replace(" ","")    
    validSequence = True
    for char in inputString :
        if char not in inputSymbols:
            validSequence = False
    if validSequence == False:
        print("The input sequence is not valid")
    else:
        currentState.append(initialState[0])
        inputString = list(inputString)
        dfa(inputString)

def getNextState(current):
    stateList =[]
    for state in states_trans:
        if state == current:
            return states_trans[state]    
    
def dfa(sequence):
    while len(sequence) > 0 :
        if len(currentState) == 1 :
            current = currentState.pop(0)
            print("Current State is : " ,current)
            print("Current input symbol :",sequence[0])
            nextState = getNextState(current)
            for value in nextState:
                if value == int(sequence[0]):
                    print("Next State =" ,nextState[value])
                    currentState.append(nextState[value])
            sequence.pop(0)
            print(sequence)
    if currentState[0] == finalState[0]:
        print("string is valid as per the DFA")
    else:
        print("String is not valid as per the DFA")
            
def dfaRun():
    option = int(input ("Select the option : 1.Test String in DFA 2. Exit"))
    if option == 1:
        inputString = str(input("Enter the pattern in 0's and 1's = "))
        initializationDFA(inputString)
    elif option == 2:
        exit()
    else:
        print("Please enter a valid input")
dfaRun()
