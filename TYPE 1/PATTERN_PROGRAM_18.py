H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
ABCDE
abcde
ABCDE
abcde
ABCDE
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    if i%2==0:
        for j in range(1,N+1):
            B=chr(j+96)
            print(B,end='')
    else:
        for j in range(1,N+1):
            A=chr(j+64)
            print(A,end='')
    print("\n")

input("PRESS ENTER TO EXIT")
