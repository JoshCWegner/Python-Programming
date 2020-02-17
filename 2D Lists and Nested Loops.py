#2D lists
#Lists in lists
#There are four elements and 3 columns in the list below
#index starts at 0
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# how to access individual elements in the list
#print(number_grid[0][0]) #index and colum to print out "1"
#print(number_grid[2][1]) #index and colum to will print out "8"

#Nested for loop to print out all of the elements in the array (2D List)
#to print out each individual element in a row
for row in number_grid:
    for column in row:
        print(column)

#to print out all of the element
for row in number_grid:
    print(row)
