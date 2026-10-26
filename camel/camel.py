cc = input("what is your name? [in camelCase]")
import re
parts = re.findall('[a-z]+|[A-Z][a-z]*', cc)
parts = [p.lower() for p in parts]
print("_".join(parts))

