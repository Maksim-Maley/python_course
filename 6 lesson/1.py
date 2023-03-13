print("#1")
a = int(input("число:"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j, end="")
    print()
    
print("#2")
for i in range(1,10):
    for j in range(1,10):
        print(i*j,end=" ")
    print()