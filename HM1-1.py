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
    print(book)
    del book[(str(input("Введите имя:")))]
else:
    print()

if args.param1:
    book[str(input("Введите имя: "))] = int(input("Введите номер: "))
    print(book)
