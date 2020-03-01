# pip install matplotlib --user
import matplotlib.pyplot as plt
import seaborn as sbn
import pandas as pd
import sqlite3
# plt.plot([2,3,4,5])
# plt.title("Hey, bro!")
# plt.xlabel("Ось x")
# plt.ylabel("Ось y")
# plt.show()

# x = [1, 2, 3, 4, 5, 6]
# y = [i**2 for i in x]
# plt.plot(x, y)
# plt.show()

# plt.plot([0, 1, 2, 3], [0, 3, 1, 2], [3, 1, 6, 4])

# data = [2, 3, 4, 5]
# plt.plot(data, color="r")
# plt.plot(data, "--")
# plt.plot(data, "*")
# plt.plot(data, "g*")

# plt.text(0, 4.5, "Очень важный комментарий", family="verdana)")

# plt.plot(data, "r--")
# plt.savefig("saved_plot.png")
# plt.show()

conn = sqlite3.connect('school.db')

table = pd.read_sql("SELECT * FROM students", conn)
table.info()
print(table)

