H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
11111
00000
11111
00000
11111
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    if i%2==0:
        for j in range(1,N+1):
            print(0,end='')
    else:
        for j in range(1,N+1):
            print(1,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
