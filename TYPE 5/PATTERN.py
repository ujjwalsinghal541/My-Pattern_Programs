H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    *
   1 2
  * * *
 1 2 3 4
* * * * *
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))
A=0

for i in range(1,N+1):
    for j in range(i,N):
        print(' ',end="")
    for j in range(1,i+1):
        if i%2==0:
            print(j,end=' ')
        else:
            print('*',end=' ')
    print("\n")
    
input("PRESS ENTER TO EXIT")
