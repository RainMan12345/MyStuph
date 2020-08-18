def x_axis(lower_bound, upper_bound):
    domain_length = upper_bound - lower_bound
    i = 0
    axis = ""
    while (i<70 and i<domain_length):
        axis+="-"
        i+=1
    return axis

def y_axis(lower_bound, upper_bound):
    domain_length = upper_bound - lower_bound
    i = 0
    axis = ""
    while (i<70 and i<domain_length):
        axis+="|\n"
        i+=1
    return axis

def replacer(line_number, space, y_list):
    j = 0
    replace_value = ""
    while j<line_number:
        replace_value+="|\n"
        j+=1
    return y_list.replace(replace_value, replace_value+ "|" + space + "\n", 1)

def spaces(line_number, spaces):
    y_list = y_axis(1,9)
    i=0
    space = ""
    while (i<spaces-1):
        space+=" "
        i+=1
    space+="."
    return replacer(line_number, space, y_list) 

print(spaces(3, 5) + "+" + x_axis(-1, 10))
