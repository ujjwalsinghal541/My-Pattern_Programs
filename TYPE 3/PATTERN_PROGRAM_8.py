H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
ABCDE
ABCD
ABC
AB
A
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(N,0,-1):
    for j in range(1,i+1):
        A=chr(j+64)
        print(A,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
