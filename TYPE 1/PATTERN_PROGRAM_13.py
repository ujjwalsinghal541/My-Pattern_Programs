H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
IHGFE
HGFED
GFEDC
FEDCB
EDCBA
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(N,0,-1):
    for j in range(i+4,i-1,-1):
        a=chr(j+64)
        print(a,end='')
    print("\n")

input("PRESS ENTER TO EXIT")
