import random
print("lets play rock,paper and scissor game")
user_score=0
computer_score=0
n=int(input("how many matches you want to play:\n"))
lst=['r','s','p']
for i in range(n,0,-1):
    user_choice = input("enter your choice 's' for scissor ,'p' for paper , 'r' for rock\n")
    computer_choice=random.choice(lst)
    print(computer_choice)
    if user_choice=='s' or user_choice=='S':
        if computer_choice=='s':
            print("it's a tie")
        elif computer_choice=='r':
            computer_score+=1
            print("i have won")
        elif computer_choice=='p':
            user_score+=1
            print("oohh no i lost")
    elif user_choice=='r' or user_choice=='R':
        if computer_choice=='s':
            computer_score+=1
            print("i have won")
        elif computer_choice=='r':
            print("it's a tie")
        elif computer_choice=='p':
            user_score+=1
            print("oohh no, i lost")
    elif user_choice=='p' or user_choice=='P':
        if computer_choice=='s':
            computer_score+=1
            print("i have won")
        elif computer_choice=='r':
            user_score += 1
            print("oohh no, i lost")
        elif computer_choice=='p':
            print("it's a tie")
    print("you have left",i-1,"matches")
print("your score",user_score)
print("my score",computer_score)
if computer_score>user_score:
    print("i won the game, you lost it.try again... ")
elif computer_score==user_score:
    print("hmm it's a tie lets play again")
else:
    print("you won the game this time but you cannot win next time")
