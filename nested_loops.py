#Loops to print tiktaktoe fields

# | | 0
#-----1 
# | | 2
# ----3
# | | 4
 
for rows in range(5):
    if rows%2 == 0:
        for column in range(1,6):
            if column%2 == 1:
                if column != 5:
                    print(" ",end="")
                else:
                    print(" ")

            else:
                print("|", end="")
        # print(" | |")
    else:
        print("-----")

