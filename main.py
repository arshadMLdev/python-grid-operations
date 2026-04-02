def grid_maker(n,m):
    grid=[]
    for i in range(n):
        print('Enter numbers for row',i+1)
        row=[]
        for j in range(m):
            number=int(input('Enter numbers for column:'))
            row.append(number)
        grid.append(row)
    print('The grid: ')
    for row in grid:
        for col in row:
            print(col,end=' ')
        print()
    return grid


def find_grid(grid,num):
    found=False
    for row in grid:
        if num in row:
            found=True
            break
    if found:
        print('Number is in the grid')
    else:
        print('Number is not in the grid')


def add_grid(grid):
    for index,row in enumerate(grid):
        addition=sum(row)
        print('Sum of row',index+1,'is:',addition)


def check_grid(grid):
    flat_list=[]
    for row in grid:
        for num in row:
            flat_list.append(num)
    unique_numbers=set(flat_list)
    if len(unique_numbers)==len(flat_list):
        print('All numbers are unique')

    else:
        print('Numbers are not unique')

grid = grid_maker(3,3)
num = int(input("Enter a number to find: "))
find_grid(grid, num)
add_grid(grid)
check_grid(grid)