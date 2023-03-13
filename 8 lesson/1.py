def ymn_ch(list):
    result=1
    for x in list:
        result=result*x
    return result
list1=[1,2,3,4]
print(ymn_ch(list1))

def povtor(list):
    print(set(list))
list2=[1,2,3,1,2,3,1,2,3]
povtor(list2)

def sravnenie(list1,list2):
    result=False
    for x in list1:
        for y in list2:
            if x == y:
                result=True
                return result
a=[1,2,3,4,5]
b=[5,6,7,8,9]
print(sravnenie(a,b))
