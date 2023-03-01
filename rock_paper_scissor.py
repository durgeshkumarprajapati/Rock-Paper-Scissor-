import random
l=['rock','paper','scissor']
u_score=0
c_score=0
while True:
    interest=input("Do you want to play game(Y/N):")
    if interest=="Y" or interest=="y":
        print('''1. for rock
                 2. for paper
                 3.for scissor''')
        u_choice=int(input("Enter your choice:"))
        c_choice=random.choice(l)
        
        if (u_choice==1 and c_choice=="rock")or(u_choice==2 and c_choice=='paper')or(u_choice==3 and c_choice=='scissor'):
            print("your choice:",u_choice)
            print("computer's choice:",c_choice)
            print("match Draw")
            c_score=c_score+1
            u_score=u_score+1
        elif (u_choice==1 and c_choice=='paper')or (u_choice==2 and c_choice=='scissor')or(u_choice==3 and c_choice=='rock'):
            print("your choice:",u_choice)
            print("computer's choice:",c_choice)
            print("computer won the match")
            c_score=c_score+1
        elif (u_choice==1 and c_choice=='scissor') or (u_choice==2 and c_choice=="rock") or (u_choice==3 and c_choice=='paper'):
            print("your choice:",u_choice)
            print("computer's choice:",c_choice)
            print("you won the match")
            u_score=u_score+1
    else:
        break
if u_score==c_score:
    print("your total score is:",u_score)
    print("computer's score is:",c_score)
    print("finally math draw")
elif u_score>c_score:
    print("your total score is:",u_score)
    print("computer's score is:",c_score)
    print("finally you are the winner!")
else:
    print("your total score is:",u_score)
    print("computer's score is:",c_score)
    print("finally computer is the winner!")
