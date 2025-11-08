def area_circle(r, pi):
    if pi == True:
        pi_hash = 3.14
    else:
        pi_hash = 1
    area = pi_hash * r ** 2
    if pi_hash == 1:
        return str(area) + "π"
    else:
        return area

print(area_circle(3,False))
