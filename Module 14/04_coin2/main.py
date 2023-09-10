def check_coin(X, Y, r):
    distance = (X ** 2 + Y ** 2) ** 0.5
    if distance <= r:
        print("\nМонетка где-то рядом")
    else:
        print("\nМонетки в области нет")

print ("Введите координаты монетки:")
coordinate_X = float(input("X: "))
coordinate_Y = float(input("Y: "))
radius = float(input("Введите радиус: "))

check_coin(coordinate_X, coordinate_Y, radius)
