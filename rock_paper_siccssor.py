import random
def game(cinput,uinput):
#Draw Secnce
    if uinput == cinput:
        return None
#Rock Sence
    elif uinput == "R":
        if cinput== "S":
            return True
        elif cinput=="P":
            return False
#Siccssor Secnce
    elif uinput == "S":
        if cinput== "P":
            return True
        elif cinput=="S":
            return False
#Paper Secnce
    elif uinput == "P":
        if cinput== "R":
            return True
        elif cinput=="S":
            return False
#Start
print("Rock Paper Siccssor")
print("R -> Rock")
print("P -> Paper")
print("S -> Siccssor")

#Computer Process
print("Computers Turn:")
Randominput = random.randint(1,3)
if Randominput == 1:
    cominput = "R"
elif Randominput == 2:
    cominput ="P"
else:
    cominput = "S"

#palyers Trun
inputuser = input("Enter your choice: ")
userinput = inputuser.upper()
result=game(cominput, userinput)

#Result
print(userinput)
print(cominput)
if result == None:
    print("It is a draw.")
elif result == True:
    print("Congratulations!!! You win.")
else:
    print("Sorry!!! You loose.")



