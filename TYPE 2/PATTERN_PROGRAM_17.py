H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
A
12
ABC
1234
ABCDE
UPTO N ROWS.'''
print(H)
num=1
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,i+1):
        if i%2==0:
            print(j,end='')
        else :
            A=chr(j+64)
            print(A,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
