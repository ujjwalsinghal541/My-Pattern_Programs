H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
A
A2
A2C
A2C4
A2C4E
UPTO N ROWS.'''
print(H)
num=1
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,i+1):
        if j%2==0:
            print(j,end='')
        else :
            A=chr(j+64)
            print(A,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
