# Q1

# a = []
# for i range(0, 10):
#   if i%2 == 1:
#     a.append(i)
# print(a)

a = []
for i in range(0, 10):
  if i % 2 == 1:
    a.append(i)

print (a)


# Q2
# class Cat:
#   def set_cat(self, n, a):
#     self.name = n
#     self.age = a
        
# cat1 = Cat()
# cat1.set_cat("Tama", 4)

# cat2 = Cat()
# cat2.set_cat("Hana" 14)

# cats = [cat1, cat2]  # リストに格納
# for c in cats
#     print(c.name, c.age)

class Cat:
  def set_cat(self, n, a):
    self.name = n
    self.age = a

cat1 = Cat()
cat1.set_cat("Tama", 4)

cat2 = Cat()
cat2.set_cat("Hana", 14)

cats = [cat1, cat2]  # リストに格納
for c in cats :
    print(c.name, c.age)