lis = []
while True:
    try:lis.append(input(" ").upper())
    except EOFError :
        break


from collections import Counter
counts = Counter(lis)
for item, count in sorted(counts.items()):
    print(count, item , end = "\n")



