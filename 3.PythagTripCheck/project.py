sides=[]

print("\n!!This is program is a Pythagorean Triples Checker!!\n")
print("when prompted, enter one side of the triangle at a time")
print("and i'll let you know if the triangle has a right angle!\n")

while True:
    ans="c"
    sides.append(input("Please Enter side 1: "))
    sides.append(input("Please Enter side 2: "))
    sides.append(input("Please Enter side 3: "))

    longest=sides.pop(sides.index(max(sides)))

    if int(longest)**2 == (int(sides[0])**2 + int(sides[1])**2):
        print("These sides make up a right angle triangle!")
    else:
        print("Sadly these sides don't form a right angle triange :(")
    while ans not in ['y', 'n']:
        ans = input("\nWould you like to try again? (y/n)")
        print("")
    if ans =="n":
        break
