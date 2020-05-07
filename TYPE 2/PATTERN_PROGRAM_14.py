H=''' THIS IS A PATTERN PROGRAM TO PRINT THIS PATTERN
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
UPTO N ROWS.'''
print(H)
num=1
N=int(input("ENTER N\n"))

for i in range(1,N+1):
    for j in range(1,i+1):
        print(num,end=' ')
        num=num+1
    print("\n")
    
input("PRESS ENTER TO EXIT")
