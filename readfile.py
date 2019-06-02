import os

"""
print("\n","=="*10,"蚂蚁庄园动态","="*10)

#打开123.txt文件
file = open('E:\999.txt','a')

#添加数据
file.write("这是写入的数据\n")

#关闭文件对象
file.flush()


with open('E:\999.txt','r') as f:
    message = f.readline()
    print(message)
    print("\n","="*29,"over","="*29,"\n")



with open('E:\999.txt','r') as f:
    number = 0                          #记录行号
    while True:
        number += 1
        line = f.readline()
        if line == '':
            break                       #跳出循环
        print(number,line,end='\n')     #输出一行内容


print("\n","="*29,"over","="*29,"\n")

with open('E:\999.txt','r') as file:
    messageall = file.readlines()
    for message in messageall:
        print(message)
"""


print(os.name)
print(os.getcwd())

with open('999.txt','r') as f:
    messageall = f.readlines()
    for message in messageall:
        print(message,end=' ')
