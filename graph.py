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
    axis = "|"
    while (i<70 and i<domain_length-1):
        axis+="\n|"
        i+=1
    return axis
print(y_axis(1,9) + x_axis(-3,9))
