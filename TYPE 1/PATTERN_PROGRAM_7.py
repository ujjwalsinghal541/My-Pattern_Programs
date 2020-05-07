H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
98765
87654
76543
65432
54321
UPTO N ROWS.'''
print(H)
N=int(input("ENTER N\n"))

for i in range(N,0,-1):
    for j in range(i+4,i-1,-1):
        print(j,end='')
    print("\n")

input("PRESS ENTER TO EXIT")
