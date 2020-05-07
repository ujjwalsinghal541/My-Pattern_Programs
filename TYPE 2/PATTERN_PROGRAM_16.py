H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
*
12
***
1234
*****
UPTO N ROWS.'''
print(H)
num=1
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,i+1):
        if i%2==0:
            print(j,end='')
        else :
            print('*',end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
