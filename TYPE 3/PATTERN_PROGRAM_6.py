H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
12345
2345
345
45
5
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(i,N+1):
        print(j,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
