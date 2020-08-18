def x_axis(domain):
    x_domain = []
    i = 0
    x_domain.append('|')
    while i<domain:
        x_domain.append(' ')
        i+=1
    return x_domain

def y_axis(x_value, y_value):
    x = x_axis(x_value)
    y = []
    i = 0
    while i<y_value:
        y.append(x)
        i+=1
    return y
print(y_axis(5,5))
