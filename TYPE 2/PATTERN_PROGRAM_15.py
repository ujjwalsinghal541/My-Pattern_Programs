H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
A
BC
DEF
GHIJ
KLMNO
UPTO N ROWS.'''
print(H)
num=1
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,i+1):
        A=chr(num+64)
        print(A,end=' ')
        num=num+1
    print("\n")
    
input("PRESS ENTER TO EXIT")
