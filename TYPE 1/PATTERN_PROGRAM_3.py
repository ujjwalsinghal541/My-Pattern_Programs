H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
11111
22222
33333
44444
55555
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,N+1):
        print(i,end='')
    print("\n")

input("PRESS ENTER TO EXIT")
