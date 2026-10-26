import sys
import csv

try:
    if not len(sys.argv) == 3 :
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
    csv_old = sys.argv[1]
    csv_new = sys.argv[2]
    if not csv_old.endswith(".csv") or not csv_new.endswith(".csv"):
        sys.exit(1)
    try:
        with open(csv_old) as file:
            old = csv.DictReader(file)
            new_s = []
            for row in old:
                new = {}
                name_full = row["name"]
                f3 = row["house"]
                f1 , f2 = name_full.split(",")
                new[1] = f1.strip()
                new[0] = f2.strip()
                new[2] = f3.strip()
                new_s.append(new)

    except FileNotFoundError:
        sys.exit(f"Could not read {csv_old}")

    try:
        with open(csv_new,"w",newline = "") as nfile:
            newrec = csv.DictWriter(nfile,fieldnames = ["first","last","house"])
            newrec.writeheader()
            for new in new_s:
                newrec.writerow({"first":new[0],"last":new[1],"house":new[2]})
            sys.exit(0)

    except FileNotFoundError:
        sys.exit(f"Could not read {csv_new}")

except IndexError:
    sys.exit(1)
