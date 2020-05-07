H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
1
23
345
4567
56789
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(i,2*i):
        print(j,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
