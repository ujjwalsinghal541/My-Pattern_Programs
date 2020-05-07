H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
12345
23456
34567
45678
56789
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(i,i+5):
        print(j,end='')
    print("\n")

input("PRESS ENTER TO EXIT")
