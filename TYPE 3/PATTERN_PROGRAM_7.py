H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
54321
4321
321
21
1
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(N,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
