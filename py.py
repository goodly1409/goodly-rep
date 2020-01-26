# class Player:
#     name = "Slim Shady"
#     age = 30
#     health = 47
#
#     def myMethod(self):
#         print("My name is", self.name)
#         print("My age", self.age)
#         print("My health", self.health)
#
#
# p = Player()
# print(p.name)
# p.myMethod()


# class Player:
#     def __init__(self):
#         self.name = "Slim Shady"
#         self.age = 25
#
#     def show(self):
#         print(self.name)
#         print(self.age)
#
#
# p = Player()
# print(p.age)
# p.show()


# class MyClass:
#   pass
#
# MyClass.x = 50
# c1, c2 = MyClass(), MyClass()
# c1.y = 10
# c2.y = 20
# print(c1.x, c1.y)
# print(c2.x, c2.y)
#
# MyClass.x = 500
# print(c1.x, c1.y)
# print(c2.x, c2.y)


# class Mydict(dict):
#     def get(self, key, default=0):
#         return dict.get(self, key, default)
#
#
# a = dict(a=1, b=2)
# b = Mydict(a=1, b=2)
#
# b['c'] = 4
# print(b)
# print(a)
# print(a.get('v'))
# print(b.get('v'))


# class Restaurant:
#     def __init__(self):
#         self.restaurant_name = "ShaWerma"
#         self.cuisine_type = "Russian"
#
#     def describe_restaurant(self):
#         print(self.restaurant_name)
#         print(self.cuisine_type)
#
#     def open_restaurant(self):
#         print("Ресторан открыт")
#
#
# r = Restaurant()
#
# print(r.restaurant_name)
# print(r.cuisine_type)
# print()
# r.describe_restaurant()
# r.open_restaurant()
#
#
# class Restaurant:
#     pass
#
#
# r1 = Restaurant()
# r2 = Restaurant()
# r3 = Restaurant()
#
# r1.restaurant_name = "Pizzeria"
# r1.cuisine_type = "Italian"
# r1.describe_restaurant()
#
# r2.restaurant_name = "Arby`s"
# r2.cuisine_type = "American"
# r2.describe_restaurant()
#
# r3.restaurant_name = "Baguette"
# r3.cuisine_type = "French"
# r3.describe_restaurant()
