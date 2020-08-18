def row(x_max):
    x = ['|']

    i = 0

    while i<x_max:
        x.append(' ')
        i += 1
    return x

def rows(x_max, y_max):
    y = []

    i = 0
    while i < y_max:
        y.append(row(x_max))
        i += 1

    y.append(row(x_max))
    return y

def plotter(x_list,y_list):
    grid = rows(10,10)
    i = 0

    while i<(len(x_list)):
        i_x = x_list[i]
        i_y = (len(grid) - 1) - y_list[i]
        grid[i_y][i_x] = '.'
        i+=1

    return draw(grid)

def draw(grid):
    string = ""
    for i in grid[:]:
        for j in i:
            string+=j
        string+='\n'
    return string

print(plotter([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,5,4,3,2]))
