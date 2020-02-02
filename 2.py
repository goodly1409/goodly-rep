# import math, datetime, module
#
# print(math.factorial(5))
#
# print(math.cos(math.pi/4))
#
# print(datetime.date(2017, 3, 21))
#
# print(module.perimetr_s(16))
#
# print(module.summ(55, 14))


# class Rest():
#     def __init__(self, a, b):
#         self.rest_name = a
#         self.cuisine_type = b
#
#     def describe_restaurant(self):
#         print(self.rest_name)
#         print(self.cuisine_type)
#
#     def open_restaurant(self):
#         print("Rest open")
#
#
# r = Rest("name", "type")
# print(r.rest_name)
# print(r.cuisine_type)
# r.describe_restaurant()
# r.open_restaurant()
#
# m = Rest("name1", "type1")
# m.describe_restaurant()
# x = Rest("name2", "type2")
# x.describe_restaurant()
# p = Rest("name3", "type3")
# p.describe_restaurant()

class User():
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.city)

    def greet_user(self):
        print("Hello, " + self.first_name + " " + self.last_name + "!")


a = User("Anton", "Shrek", 25, "Moscow")
a.describe_user()
a.greet_user()
d = User("Danya", "Ivanov", 25, "Kiev")
d.describe_user()
d.greet_user()
s = User("Sasha", "Smirnov", 25, "Tomsk")
s.describe_user()
s.greet_user()


