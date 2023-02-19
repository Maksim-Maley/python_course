print("задание 1")
a=0
b=int(input("Укажите число:"))
for i in range(13,b):
    a+=i
print (a)

print("задание 2")
b=int(input("Укажите число:"))
for i in range(0,b,2):
    print(i)

print("задание 3")
a=0
b=int(input("Укажите число:"))
for i in range(0,b,3):
    a+=i
print(a)


print("доп. задание")
a=["S","T","A","LK","ER"]
for i in a:
    print(i, end=".")