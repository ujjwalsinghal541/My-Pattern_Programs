H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
AAAAA
BBBB
CCC
DD
E
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,N-i+2):
        A=chr(i+64)
        print(A,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
