def dodaj(a , b):
    return a+b

def odejmij (a,b):
    return a-b


if __name__=="__main__":
    a = float(input("podaj a"))
    b = float(input("podaj b"))
    print(dodaj(a,b))
    print(odejmij(a,b))