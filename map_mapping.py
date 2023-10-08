# In this assignment, we write a program that will mark a spot on a map with an X.

# This map contains a nested list as follows. 

# map = [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# we've used this line of code print(f"{map[0]}\n{map[1]}\n{map[2]}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

      A      B     C
# 1  ['⬜️', '⬜️', '⬜️']

# 2  ['⬜️', '⬜️', '⬜️']

# 3  ['⬜️', '⬜️', '⬜️']

# Now it looks a bit more like the coordinates of a real map.

# Your job is to write a program that allows you to mark a square on the map using a letter-number system.

# So an input of A3 should place an X at the position shown below:

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['X', '⬜️', '⬜️']

# And an input of C1 should place an X at the position shown below:

# ['⬜️', '⬜️', 'X']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']


# Solution
===============================================

map = [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]


input = 'B2'
input = list(input)

first_cord = input[0]
second_cord = input[1]
lst = int(second_cord) - 1

index = {"A": 0, "B": 1, "C": 2}

position = index.get(first_cord)

map[lst].pop(position)
map[lst].insert(position, 'X')

print(f"{map[0]}\n{map[1]}\n{map[2]}")

    ['⬜️', '⬜️', '⬜️']

    ['⬜️', '⬜️', '⬜️']

    ['⬜️', '⬜️', '⬜️']
