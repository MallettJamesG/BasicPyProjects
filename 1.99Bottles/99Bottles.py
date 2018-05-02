
for i in range(99,0,-1):
    if i-1==1:
        print(i," bottles of beer on the wall, ",i," bottles of beer. Take one down,"
                "pass it around,", i-1, "bottle of beer on the wall\n")
    elif i-1==0:
        print(i," bottle of beer on the wall, ",i," bottle of beer. Take one down,"
                "pass it around, no more bottles of beer on the wall\n")
    else: print(i," bottles of beer on the wall, ",i," bottles of beer. Take one down,"
            "pass it around,", i-1, "bottles of beer on the wall\n")
