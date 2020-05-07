H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
ABCDE
BCDE
CDE
DE
E
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(i,N+1):
        A=chr(j+64)
        print(A,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
