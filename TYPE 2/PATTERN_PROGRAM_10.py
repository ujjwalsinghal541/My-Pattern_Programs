H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
E
DD
CCC
BBBB
AAAAA
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(N,0,-1):
    for j in range(N,i-1,-1):
        A=chr(i+64)
        print(A,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
