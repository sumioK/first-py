# function
def say_hello():
  print("Hello, world!")

say_hello()

def say_gm():
  print("Good Morning!")

say_gm()
say_gm()
say_gm()

# 引数 (関数の外部から内部に値を渡す)
def say_number(a):
  print(a)

say_number(123)

def add(a, b, c):
  d = a + b + c
  print(d)

add(3, 4, 5)


# 返り値 (関数の内部から外部に値を渡す)
def get_number():
  a = 123
  return a

b = get_number()
print(b)

# 引数と返り値
def add(a, b):
  c = a + b
  return c

result1 = add(3, 4)
print(result1)
result2 = add(7, 8)
print(result2)


# 変数のスコープ
# 関数内で定義された変数がローカル変数、関数外で定義された変数がグローバル変数
glob_1 = 123

def show_number():
  loc_1 = 456
  print(glob_1, loc_1)

show_number()

# local変数には関数外からアクセスできない
glob_2 = 123
def setNum():
  local_2 = 456
setNum()
# print(glob_2, loc_2)



# class 複数の関数のようなもの(メソッド)をまとめることができる
class Calc:
  def add(self, a, b):
    print(a + b)

  def multiply(self, a, b):
    print(a * b)
  #インスタンスの作成 
cl = Calc()
cl.add(2, 3)
cl.multiply(4, 5)


class Box:
  def set_number(self, n1, n2):
    self.num1 = n1
    self.num2 = n2
# インスタンスの作成
bx = Box()
bx.set_number(123, 456)
print(bx.num1)
print(bx.num2)
bx.num1 = 999
print(bx.num1)


class Dog:
  def set_dog(self, n, a):
    self.name = n
    self.age = a
# インスタンスの作成
dog1 = Dog()
dog1.set_dog("pochi", 5)
# インスタンスは複数作成できる
dog2 = Dog()
dog2.set_dog("Hachi", 12)
# リストにインスタンスを入れる
dogs = [dog1, dog2]
for d in dogs:
  print(d.name, d.age)

# ファイルの保存と読み込み
# 保存
# greetings = "Good morning! Good night!"

# with open("greetings.text", "w") as f:
#   f.write(greetings)

# 読み込み
with open("greetings.text", "r") as f:
  print(f.read())