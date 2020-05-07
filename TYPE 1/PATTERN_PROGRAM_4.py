H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
55555
44444
33333
22222
11111
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(N,0,-1):
    for j in range(1,N+1):
        print(i,end='')
    print("\n")

input("PRESS ENTER TO EXIT")
