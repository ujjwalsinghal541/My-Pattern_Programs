H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
ABCDE
ABCDE
ABCDE
ABCDE
ABCDE
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(65,N+65):
        a=chr(j)
        print(a,end='')
    print("\n")

input("PRESS ENTER TO EXIT")
