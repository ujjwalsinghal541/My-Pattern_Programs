H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
    5
   44
  333
 2222
11111
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(N,0,-1):
    for j in range(i-1,0,-1):
            print(' ',end='')
    for j in range(N,i-1,-1):
            print(i,end='')
    print("\n")
    
input("PRESS ENTER TO EXIT")
