H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
10101
1010
101
10
1
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,N-i+2):
        if j%2==0:
            print('0',end='')
        else:
            print('1',end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
