#Loops to print tiktaktoe fields in Python

# | | 0
#-----1 
# | | 2
# ----3
# | | 4
 
for rows in range(5): # 0, 1, 2, 3, 4
    if rows%2 == 0:
        for column in range(1,6): #1, 2, 3, 4, 5
            if column%2 == 1:
                if column != 5:
                    print(" ",end="") #1, 3
                else:
                    print(" ") #5

            else:
                print("|", end="")#2
        # print(" | |")
    else:
        print("-----")

