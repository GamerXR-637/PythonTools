def reflect_x(x,y,n):
    if x == "" or y == "" or n == "":
        return "One or more value are no filled"
    elif isinstance(x, str) == True or isinstance(y, str) == True or isinstance(n, str) == True:
        return "One or more is a String please input a number"
    else:
        px = 2 * n - x
        return px , y

print(reflect_x(3,4,5))