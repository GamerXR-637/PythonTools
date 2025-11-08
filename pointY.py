def reflect_y(x,y,n):
    if x == "" or y == "" or n == "":
        return "One or more value are no filled"
    elif isinstance(x, str) == True or isinstance(y, str) == True or isinstance(n, str) == True:
        return "One or more is a String please input a number"
    else:
        ry = 2 * n - y
        return x , ry

print(reflect_y(3,4,5))