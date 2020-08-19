def circlie_area(x):
    num = x * x * 3.14
    return num

def circle_circum(a):
    num = a * 2 * 3.14
    return num

n = int(input('半徑:'))
b = circle_circum(n)
n = circlie_area(n)

print('圓面積',n)
print('圓周長',b)
