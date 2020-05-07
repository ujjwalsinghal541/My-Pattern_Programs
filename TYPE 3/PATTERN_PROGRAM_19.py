H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
11111
0000
111
00
1
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,N-i+2):
        if i%2==0:
            print('0',end='')
        else:
            print('1',end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
