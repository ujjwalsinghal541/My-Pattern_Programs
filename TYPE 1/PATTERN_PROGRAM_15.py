H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
ABCDE
FGHIJ
KLMNO
PQRST
UVWXY
UPTO N ROWS.'''
print(H)
k=0
N=int(input("ENTER N\n"))

for i in range(1,N*5,k+5):
    for j in range(i,i+5):
        A=chr(j+64)
        print(A,end=' ')
    print("\n")

input("PRESS ENTER TO EXIT")
