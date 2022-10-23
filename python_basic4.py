# __init__メソッド　→　インスタンス生成時に、初期設定を行う
class Calc:
  def __init__(self, a):
    self.a = a

  def add(self, b):
    print(self.a + b)

  def multiply(self, b):
    print(self.a * b)

cl = Calc(3) #initメソッドでaに3を代入
cl.add(4)
cl.multiply(4)




# __call__メソッド　→　メソッドの名前を使わずインスタンス名を使って呼び出す

class Calc1:
  def __init__(self, a):
    self.a = a
  def __call__(self, c):
    print(self.a * c + c)
  def add(self, b):
    print(self.a + b)
  def multiply(self, b):
    print(self.a * b)

cl1 = Calc1(3)
cl1(5)
