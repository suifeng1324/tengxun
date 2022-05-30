import os

str = "this is really a string example....wow!!!"
name2= 36

print("-------------------------1------------------")

print(str.capitalize())              # str字符串转大写,结果This is really a string example....wow!!!
print(str.isdigit())                # 判断str是否为数字,结果False
print(str.rfind("h"))                # 返回字符串最后一次出现的位置，如果没有匹配项则返回-1，结果1
print("您好")

if str.isdigit():
    print("yes")
else:
    print("no")

fo = open(r"D:\1.txt","w")
print("filename:",fo.name[fo.name.rfind("\\")+1:])
print("filename:",fo.name[:fo.name.rfind("\\")+1])
fo.write("adfdf!\nlll\r")
fo.close()
print(os.getcwd())
os.mkdir(r"test")

