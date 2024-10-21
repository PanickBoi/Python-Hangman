import random
import os
from pathlib import Path
print('Get current working directory : ', os.getcwd())
words =[]
words_file = os.path.dirname(__file__)+"\Words.txt"
file = open(words_file,"r")
while True:
    line_content = file.readline()
    if not line_content:
        break
    else:
        line_content = line_content.strip("\n")
        line_content_array = [char for char in line_content]
        if line_content_array[0] != " " and line_content_array[-1] != " ":
            words.append(line_content)
file.close()
chosen_word = ""
guess_word = []
cw_list = []
Guesses = 0
stages=[
'''
        __ __ __
                    |
                    |
                    |
                    |
                    |

''',
'''
        __ __ __
                    |
        O          |
                    |
                    |
                    |

''',

'''
        __ __ __
                    |
        O          |
         |          |
         |          |
                    |

''',
''''
        __ __ __
                    |
        O          |
       / |          |
         |          |
                    |

''',
''''
        __ __ __
                    |
        O          |
       / | \        |
         |          |
                    |

''',
''''
        __ __ __
                    |
        O          |
       / | \        |
         |          |
        /           |

''',
''''
        __ __ __
                    |
        O          |
       / | \        |
         |          |
        / \         |

''',
''''
        __ __ __
         |          |
        O          |
       / | \        |
         |          |
        / \         |

''',
    ]
#MISC
#----<>-----------<>----#

def punish():
    global stages,Guesses
    if Guesses < 8:
        print(stages[Guesses])
    Guesses += 1

    
def checkRight():
    global guess_word,cw_list
    if guess_word != cw_list:
        punish()

        
def SUGW(word):
    global guess_word
    for i in word:
        if i != " ":
            guess_word.append("_")
        else:
            guess_word.append(" ")

            
def ReplaceElement(array,index,replacer):
    array.pop(index)
    array.insert(index,replacer)
    return array

#ANSWER FNCTION
#----<>-----------<>----#
def checkAnswer(user_word):
    global guess_word,cw_list,Guesses
    i = 0
    count = 0
    if len(user_word) == len(chosen_word):
        for letter in user_word:
            if letter == cw_list[i]:
                i += 1
            else:
                punish()
                break
        if list(user_word) == cw_list:
            guess_word = list(user_word)
        else:
            print("Wrong Word!")
            punish()
    elif len(user_word) == 1:
        for letter in cw_list:
            if user_word == letter:
                ReplaceElement(guess_word,i,letter)
                count += 1
            i += 1
        if count == 0:
            punish()
    else:
        print("Invalid Input! (Guess either a LETTER or the ENTIRE WORD) \n There's still a penalty!")
        punish()
    print("Guessed word: "," ".join(guess_word),"\n","<>"*20)
    
 #RE-DO FUNCTION#
#----<>-----------<>----#
def regame():
    print("Do you wanna go again?")
    user_choice = input("(Y/N): ")
    if user_choice.lower() == "y":
        game()
    elif user_choice.lower() == "n":
        quit()
    else:
        print("WRONG INPUT DUMBASS")
        regame()
#GAME FUNCTION
#----<>-----------<>----#
def game():
    global chosen_word,words,guess_word,cw_list,Guesses,user_word
    chosen_word = words[random.randrange(0,len(words))].lower()
    guess_word = []
    cw_list = list(chosen_word)
    Guesses = 0
    print("<>"*20,"\n Guess the word!")
    SUGW(chosen_word)
    print(" ".join(guess_word))
    while True:
        if Guesses < 8 and cw_list != guess_word:
            user_word = input("Guess: ")
            checkAnswer(user_word.lower())
        elif Guesses >= 8:
            print("You Lost,correct word: ",chosen_word)
            regame()
            break
        else:
            print("You won!")
            regame()
            break
game()
