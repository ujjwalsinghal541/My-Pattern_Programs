H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
12345
12345
12345
12345
12345
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(0,N):
    for j in range(1,N+1):
        print(j,end='')

    print("\n")

input("PRESS ENTER TO EXIT")
