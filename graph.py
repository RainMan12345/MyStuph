def user_input():
    lower_bound = input("Enter lower bound: ")
    upper_bound = input("Enter upper bound: ")
    return x_axis(int(lower_bound), int(upper_bound))

def x_axis(lower_bound, upper_bound):
    print_amount = upper_bound - lower_bound
    i = 0
    dash = "-"
    axis = ""
    while (i<70 and i<print_amount):
        axis+=dash
        i+=1
    print(axis)

user_input()
