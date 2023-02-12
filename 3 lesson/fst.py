a = int(input("введите число:"))

if a > 100:
    print('число больше 100')
elif a < 100 and a > 50:
    print("число больше 50, но меньше 100")
elif a < 50:
    print("число меньше 50")
elif a == 100:
    print("число 100")
elif a == 50:
    print("число 50")

a = int(input("укажите ваш возраст:"))

if a >= 18:
    print("входите")
else:
    print("ваш возраст не соответствует требованиям")

a = int(input("первое число:"))
b = int(input("второе число:"))

if a < b:
    print(a)
else:
    print(b)