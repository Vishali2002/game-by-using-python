import random

def game(comp,you):
    if comp == you:
        None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "s":
            return True
        elif you == "g":
            return False
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True
    

rand = random.randint(1, 3)
print(rand)
print("Computer Turn for \n 1.snake(s) \n 2.gun(g) \n 3.water(w)")
print("Your Turn for \n 1.snake(s) \n 2.gun(g) \n 3.water(w)")
you = input(" ")

if rand == 1:
    comp = "s"
elif rand == 2:
   comp = "g"
else:
    comp = "w"
a = game(comp,you)
print(f"computer choose : {comp}")
print(f"you choose :{you}")

if a==None:
    print("The game is tie")
elif a:
    print("You win")
else:
    print("You lose")
