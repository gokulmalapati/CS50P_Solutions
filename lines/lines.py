#importing all of the modules
import sys
import csv

i = 0
try:
    test_file = sys.argv[1]
    if  not test_file.endswith(".py") or len(sys.argv)>2:
        raise ValueError

    else:
        with open(test_file) as file:
            for line in file :
                line_str = line.strip()
                if line_str.startswith("#"):
                    pass
                elif not line_str:
                    pass
                else:
                    i += 1
        print(i)
except IndexError:
    sys.exit(1)
except ValueError:
    sys.exit(1)
except FileNotFoundError:
    sys.exit(1)
