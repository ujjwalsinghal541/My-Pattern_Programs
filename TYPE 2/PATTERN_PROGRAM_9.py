H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
A
BB
CCC
DDDD
EEEEE
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,i+1):
        A=chr(i+64)
        print(A,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
