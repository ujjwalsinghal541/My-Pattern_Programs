H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    1
   10
  101
 1010
10101
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))
A=0
for i in range(1,N+1):
    for j in range(N,i,-1):
            print(' ',end='')
    for j in range(1,i+1):
            if j%2==0:
                print('0',end='')
            else:
                print('1',end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
