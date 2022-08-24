def rps_game(p1,p2):
    if(p1==p2):
        return "tie"
    elif (p1 == "rock" or p2 == "scissor") and (p1 == "paper" or p2 == "rock") and (p1 == "scissor" or p2 == "paper"):
        return p1 + "wins"
    elif(p1=="scissor" or p2=="rock") and (p1=="rock" or p2=="paper") and (p1=="paper" or p2=="scissor"):
        return p2 + "wins"
    else:
        return "invalid"

p1=input("enter:")
p2=input("enter:")
set=rps_game(p1,p2)
print(set)