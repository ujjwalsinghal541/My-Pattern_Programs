H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    1
   32
  543
 7654
98765
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(N-i,0,-1):
            print(' ',end='')
    for j in range(2*i-1,i-1,-1):
            print(j,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
