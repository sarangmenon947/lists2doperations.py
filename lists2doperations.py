numbers = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(numbers)

length = len(numbers)

for i in range(0, length):
    for j in range(0, len(numbers[0])):
        print(numbers[i][j], end = " ")
    print()

rows = int(input("Enter the number of rows you want "))
column = int(input("Enter the number of columns you want "))
blanklist = []


for i in range(rows):
    temp = []
    for j in range(column):
        x = int(input ("Enter the element of the list "))
        temp.append(x)
    blanklist.append(temp)
    
for i in range(rows):
    for j in range(column):
        print(blanklist[i][j], end = " ")
    print()