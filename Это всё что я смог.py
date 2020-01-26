import argparse
import sys

from pip._vendor.distlib.compat import raw_input

book = {"Masha": 89778081539, "Dasha": 89772381536, "Pasha": 89778081476, "Sasha": 89778088236, "Natasha": 89771231536}

parser = argparse.ArgumentParser(description='Book')
parser.add_argument('-a', "--add", dest="param1")
parser.add_argument('-d', "--delete", dest="param2")
parser.add_argument('-s', "--show", dest="param3")

args = parser.parse_args()

if args.param3:
    z = input("Введите запрос:")
    if z in book.keys():
        print(book[z])
    else:
        print()
else:
    print()
if args.param2:
    book.pop(str(input('')), int(input()))
else:
    print()

print(args)


# TypeError: 'NoneType' object is not callable
# TypeError: 'str' object is not callable
# AttributeError: 'Namespace' object has no attribute 'show'
#
# Это максимум, что я смог сделать.
#
# 'Namespace' object has no attribute 'show' про эту ошибку написано в интернете, что это баг Pyhton 3, как её решить - я не знаю.
#
# :с
