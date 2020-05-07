H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
12345
1234
123
12
1
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,N-i+2):
        print(j,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
