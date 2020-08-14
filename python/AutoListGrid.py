'''This program print the character picture of the grid.'''

grid=[['.','.','.','.','.','.'],
      ['.','0','0','.','.','.'],
      ['0','0','0','0','.','.'],
      ['0','0','0','0','0','.'],
      ['.','0','0','0','0','0'],
      ['0','0','0','0','0','.'],
      ['0','0','0','0','.','.'],
      ['.','0','0','.','.','.'],
      ['.','.','.','.','.','.']]


for i in range(len(grid)):
    for n in range(len(grid[i])):
        print(grid[i][n],end='')
    print()
print()

for c in range(len(grid)):
    for m in grid[c]:
        print(m,end='')
    print()

