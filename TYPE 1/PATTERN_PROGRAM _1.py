H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
*****
*****
*****
*****
*****
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(0,N):
    for j in range(0,N):
        print("*",end='')

    print("\n")

input("PRESS ENTER TO EXIT")
