import random 
def introduction():
    """this function greets the user and asks him to guess a character """
    name= input ("what is your name:")
    print ("Good luck",name)
    print ("guess the characters :")
def choose():
    """This function make a lisit of word and make the computer choose random word from it by random.choice"""
    words = ['rainbow', 'computer', 'science', 'programming',  
            'python', 'mathematics', 'player', 'condition',  
            'reverse', 'water', 'board', 'geeks']  
    word = random.choice (words)
    return word
def loose():
    """"This function sees if the user finish his turns and still did not guess the word means the user loose"""
    global turns
    if turns == 0:
        print("You Loose")
def thesectword():
    """This functioncompare the guesses characters the user enter it with the character of the word choosen """ 
    global char
    global word
    global failed
    strer=""
    for char in word :
        if char in guesses :
            strer+=char
        else :
             strer+="_" 
             failed +=1
        strer+=" "
    print(strer)
def won():
    """"This function sees the no of times the user fail if it is equal to zero will print win and tell him the word """
    global failed
    global word
    if failed == 0 :
        print ("you win ")
        print ("the word is ",word )
    return failed == 0 
def wrongAnser():
    """"This function sees if the user enter wrong answer will decrement the turns by one and tell him how many turns are left"""
    global guess
    global word
    global turns
    if guess not in word: 
          turns -= 1
          print("Wrong") 
          print ("you have ",+turns,"more guesses")
def inputuser():
    """"This function asks the user to enter another character and compare it with the guesses if the user enter it before will tell him if not will put it in the guesses"""
    key=0
    global guess
    global guesses
    while key ==0:
        guess = input("guess a character:") 
        if guess in guesses:
            print("You enter this before")
        else:
            guesses += guess  
            key=1
#main
introduction()
word=choose()
guesses = '' 
turns = 12
while turns > 0 :    
    failed = 0
    thesectword()
    if won():
        break 
    inputuser()
    wrongAnser()
    loose()