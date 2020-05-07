H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
55555
4444
333
22
1
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(N,0,-1):
    for j in range(i,0,-1):
        print(i,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
