a = int(input("1-Son: "))
b = int(input("2-Son: "))
c = int(input("3-Son: "))
d = int(input("4-Son: "))
e = int(input("5-Son: "))

def sonlar(a, b, c, d, e):
    if a > b and a > c and a > d and a > e:
        return (a, "Katta")
    elif b > a and b > c and b > d and b > e:
        return (b, "Katta")
    elif c > a and c > b and c > d and c > e:
        return (c, "Katta")
    elif d > a and d > b and d > c and d > e:
        return (d, "Katta")
    else:
        return (e, "Katta")
print(sonlar(a, b, c, d, e))

