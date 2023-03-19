def read_file(x):
  with open(x) as file_1:
    read_file = file_1.read()
    print(read_file)
file = "test.txt"
read_file(file)

import os
def list_les(lis):
  print(os.listdir(lis))
list = "C://Users/makvi/OneDrive/Рабочий стол/Python/python_course/9 lesson"
list_les(list)

import re
def file_num(fil1,fil2):
  with open(fil1,"r") as file_1:
    with open(fil2,"w") as file_2:
      for i in file_1:
        num = re.findall(r"\b[1-9][0-9]* \b", i)
        if num:
          file_2.write(" ".join(num) + "\n")
file_num("1.txt","2.txt")
