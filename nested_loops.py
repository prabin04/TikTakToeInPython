#Loops to print tiktaktoe fields in Python

# | | 0
#-----1 
# | | 2
# ----3
# | | 4
 
for rows in range(5): # 0, 1, 2, 3, 4
    if rows%2 == 0:
        for column in range(1,6): #1, #2, #3, #4, #5
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

