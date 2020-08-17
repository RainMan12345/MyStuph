def x_axis(lower_bound, upper_bound):
    domain_length = upper_bound - lower_bound
    i = 0
    axis = ""
    while (i<70 and i<domain_length):
        axis+="-"
        i+=1
    return axis

print(x_axis(-3,9))
