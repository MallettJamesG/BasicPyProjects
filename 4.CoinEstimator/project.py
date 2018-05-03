import math

print("\nCoin Estimator!\n")
print("Enter the total weight of your coins and I'll estimate the following for you:")
print("1. How many wrappers you'll need")
print("2. How many coins you have")
print("3. Total value of your coins\n")

inp = input("Would you like to use grams(1) or pounds(2)? (Default = grams)")

pen = input("\nEnter total weight of your pennies: ")
nick = input("Enter total weight of your nickels: ")
dim = input("Enter total weight of your dimes: ")
quar = input("Enter total weight of your quarters: ")

if int(inp)==2:
    pen = int(pen)*453.59237
    nick = int(nick)*453.59237
    dim = int(dim)*453.59237
    quar = int(quar)*453.59237

numpen = int(math.ceil(int(pen)/2.5))
numnick = int(math.ceil(int(nick)/5))
numdim = int(math.ceil(int(dim)/2.268))
numquar = int(math.ceil(int(quar)/5.670))

penwrap = math.ceil(numpen/50)
nickwrap = math.ceil(numpen/40)
dimwrap = math.ceil(numpen/50)
quarwrap = math.ceil(numpen/40)

worth = (numpen + numnick*5 + numdim*10 + numquar*25)/100

print("\nYou have roughly ",numpen," pennies, ",numnick," nickels, ",numdim," dimes and "
      ,numquar, "quarters. ",(numpen+numnick+numdim+numquar)," coins in total!")
print("Thats worth $",round(worth,2))
print("So you will need the following number of wrappers: ")
print(penwrap," penny wrappers, ",nickwrap," nickel wrappers, ",dimwrap,
      " dime wrappers and ",quarwrap," quarter wrappers")
