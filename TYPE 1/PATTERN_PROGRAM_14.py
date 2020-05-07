H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15 
16 17 18 19 20
21 22 23 24 25 
UPTO N ROWS.'''
print(H)
k=0
N=int(input("ENTER N\n"))

for i in range(1,N*5,k+5):
    for j in range(i,i+5):
        print(j,end=' ')
    k=i
    print("\n")

input("PRESS ENTER TO EXIT")
