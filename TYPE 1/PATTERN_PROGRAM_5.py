H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
54321
54321
54321
54321
54321
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(N,0,-1):
    for j in range(N,0,-1):
        print(j,end='')
    print("\n")

input("PRESS ENTER TO EXIT")
