def fun_sum(x,y):
    if x > y:
        x,y=y,x
    a=0
    for i in range(x,y+1):
      a+=i
    return a
a=int(input("1 число: "))
b=int(input("2 число: "))
print(fun_sum(a,b))

def name_soname(x,y):
   print("Привет")
   print(x,y)
name=input("Имя: ")
soname=input("Фамилия: ")
name_soname(name,soname)

def p_p(x,y):
   a=2*(x+y)
   b=x*y
   return a,b
a=int(input("1:"))
b=int(input("2:"))
print(p_p(a,b))