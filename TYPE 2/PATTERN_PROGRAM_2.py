H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
1
12
123
1234
12345
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,i+1):
        print(j,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
