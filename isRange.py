def is_range(x,y,Value):
    if x <= Value <= y:
        return True
    else:
        return False

print(is_range(3,5,2))