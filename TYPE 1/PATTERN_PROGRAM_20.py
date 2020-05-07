H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
A2C4E
A2C4E
A2C4E
A2C4E
A2C4E
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,N+1):
        if j%2==0:
            print(j,end="")
        else:
            A=chr(j+64)
            print(A,end="")
    print("\n")

input("PRESS ENTER TO EXIT")
