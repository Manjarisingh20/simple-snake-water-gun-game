import random
computer_score=0
user_score=0
i=0
for i in range (5):
 options = ["snake", "water", "gun"]
 computer = random.choice(options)
 player= input("enter snake , water or gun\n")

 if computer=="snake":
    if player=="water":
        print("computer choose",computer)
        print("you loose")
        computer_score += 1
    elif player=="gun":
        print("computer choose",computer)
        print("you win")
        user_score +=1
    else:
        print("computer choose",computer)
        print("tie")
        computer_score +=1
        user_score +=1
 elif computer=="water":
    if player=="snake":
        print("computer choose ",computer)
        print("you win")
        user_score +=1
    elif player=="gun":
        print("computer choose",computer)
        print("you loose")
        computer_score += 1
    else:
        print("computer choose",computer)
        print("tie")
        computer_score +=1
        user_score +=1
else:
    if player=="snake":
        print("computer choose",computer)
        print("you loose")
        computer_score += 1
    elif player=="gun":
        print("computer choose",computer)
        print("tie")
        computer_score +=1
        user_score +=1
    else:
        print("computer choose",computer)
        print("you win")
        user_score +=1

print("computer score is =",computer_score)
print("user score is =",user_score)


if computer_score > user_score:
  
  print("shittt!! computer wins")
elif user_score > computer_score:
  print("yayyy!! you win ")
else:
  print("tie")
