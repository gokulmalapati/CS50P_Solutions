import sys
import csv
from tabulate import tabulate

try:
    path = sys.argv[1]
    if not len(sys.argv) == 2 or not path.endswith(".csv"):
        raise ValueError
    with open(path) as file:
        menu = csv.DictReader(file)
        print(tabulate(menu,headers="keys",tablefmt = "grid"))


except IndexError:
    sys.exit(1)
except ValueError:
    sys.exit(1)
except FileNotFoundError:
    sys.exit(1)

