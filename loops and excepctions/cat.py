"""i = 0
while i < 3:
    print("meow")
    i += 1
"""

#for _ in range(300000):
 
 #   print("meow")

#print("meow \n" *3 , end= "")



"""
while True:
    n = int(input ("What's in n?: "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
"""



def main():
    number = getnumber()
    meow(number)

def getnumber():
    while True:
        n = int(input ("What's in n?: "))
        if n > 0:
            return n
            break
        
def meow(n):
    for _ in range(n):
        print("meow") 
main()

