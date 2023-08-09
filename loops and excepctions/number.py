def main():
    x = get_int("What's x?")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            #x = int( input ("What's x? ")) cualquiera de las 2 es correcta
            return int( input (prompt))
        except ValueError:
            #print("x is not an integer")
            pass
        #else:
            #break y dejar fuera el return en otro caso
         #   return x
main()  