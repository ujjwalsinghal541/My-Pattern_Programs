H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
ABCDE
BCDEF
CDEFG
DEFGH
EFGHI
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(i,i+5):
        a=chr(j+64)
        print(a,end='')
    print("\n")

input("PRESS ENTER TO EXIT")
