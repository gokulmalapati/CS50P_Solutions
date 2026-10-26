import sys
from PIL import Image,ImageOps

try:
    if not len(sys.argv) == 3 :
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
    pic_old = sys.argv[1]
    pic_new = sys.argv[2]
    valid_ext = (".jpg" , ".jpeg" , ".png")
    if not pic_new.lower().endswith(valid_ext) or not pic_old.lower().endswith(valid_ext) :
        sys.exit(1)
    if pic_new.lower().split(".")[-1] != pic_old.lower().split(".")[-1]:
        sys.exit("Input and output have different extensions")
    old = Image.open(pic_old)
    shirt = Image.open("shirt.png")

    target_size = shirt.size
    fitted_old = ImageOps.fit(old,target_size)
    fitted_old.paste(shirt , (0,0),mask = shirt)
    fitted_old.save(pic_new)
    sys.exit(0)

except FileNotFoundError:
    sys.exit("Input does not exist")
except IndexError:
    sys.exit(1)
