# list
from turtle import end_fill


a = [2011, 2012, 2013, 2014, 2015]

print(a[0])
print(a[1])
print(a[2])

b = 2016
c = [b, 2017, 20.1, "hello", "hi"]
print(c[1:4])

# リストの要素にリストを入れる
d = [[2012, 2013, 2014], [2015, 2016, 2017]]
print(d[0])
print(d[1][1])

# 要素の変更
e = ["py", 543.21, 79, "thon",[2018, 2019, 2020]]
print(e)
e[2] = 99
print(e)
# 要素の追加
e.append(2021)
print(e)

# tuple　リストと違い後から変更できない
a = [2012, 2013, 2014]
b = (2012, 2013, 2014)
print(a)
print(b)
print(a[1])
print(b[1])

a[1] = 2016
print(a)
# b[1] = 2016
# print(b) 

a.append(2015)
print(a)
# b.append(2015)
# print(b)

# 辞書
a = {"Taro":1985, "Hanako":1986}
print(a["Taro"])

a["Hanako"] = 1987
print(a)

a["Jiro"] = 1989
print(a)

# if文
a = 5
if a == 5:
  print("3+4=")
  print(3 + 4)
else:
  print("3×4=")
  print(3 * 4)

b = 4
if b < 3:
  print("Hello!")
elif b < 5:
  print("Hi!")
else:
  print("Yeah!")

time = 20
if time < 12:
  print("Good morning!")
elif time < 17:
  print("Good afternoon!")
elif time < 21:
  print("Good evening!")
else:
  print("Good night!")