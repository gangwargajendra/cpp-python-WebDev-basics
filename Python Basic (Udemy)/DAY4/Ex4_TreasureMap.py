row1 = [" " , " " , " "]
row2 = [" " , " " , " "]
row3 = [" " , " " , " "]

map = [row1 , row2 , row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the truesure? col & row : ")

col = int(position[0])
row = int(position[1])

# 1-base indexing
map[row-1][col-1] = "X"

print(f"{row1}\n{row2}\n{row3}")