H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
EEEEE
DDDDD
CCCCC
BBBBB
AAAAA
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(N,0,-1):
    for j in range(1,N+1):
        a=chr(i+64)
        print(a,end='')
    print("\n")

input("PRESS ENTER TO EXIT")
