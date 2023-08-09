import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: #slice, para recortar el ultimo dato -1
    print("hello, my name is", arg)
