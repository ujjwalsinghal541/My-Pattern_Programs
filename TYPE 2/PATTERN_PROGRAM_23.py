H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
0
10
101
0101
01010
UPTO N ROWS.'''
print(H)
num=1
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print('0',end='')
        else :
            print('1',end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
