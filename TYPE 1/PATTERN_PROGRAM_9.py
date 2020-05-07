H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
AAAAA
BBBBB
CCCCC
DDDDD
EEEEE
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,N+1):
        a=chr(i+64)
        print(a,end='')
    print("\n")

input("PRESS ENTER TO EXIT")
