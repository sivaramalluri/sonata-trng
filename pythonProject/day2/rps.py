p1=input()
p2=input()
if(p1==p2):
    print("no player win")
elif((p1=="rock" and p2=="scissors") or (p1=="paper" and p2=="scissors") or(p1=="paper" and p2=="rock")):
    print("p1 wins")
else:
    print("p2 wins")