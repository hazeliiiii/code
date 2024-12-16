# list of whats needed:
# 20 diff random numbers
# 4 random signs per question

from random import *
flag = 1
score = 0

def question_ask():
    while flag == 1:
        try:
            answer = int(input("What is the answer? "))
            return (answer)
        except ValueError:
            print ("Needs to be an integer!")
            
def questions():
    x = randint(1,10)
    y = randint(1,10)
    z = randint(1,3)    
    
    if z == 1:
        solution = x + y
        sign = "+"
    elif z == 2:
        solution = x - y
        sign = "-"
    elif z == 3:
        solution = x * y
        sign = "x"
        
    print("What is", str(x), str(sign), str(y)+"?")
    u_input = question_ask()
        
    if u_input == solution:
        print("Correct!")
        global score
        score = score + 1
    else:
        print("Incorrect! The answer was:", solution)
        score = score
            
name = input("What is your name? ")
amount = int(input("How many questions do you want to do?"))

for i in range(1,amount):
    questions()
    
print ("You got", score, "/", amount)
