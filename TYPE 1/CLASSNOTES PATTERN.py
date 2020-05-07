n=int(input("ENTER N:"))

for i in range(0, n):      # inner loop to handle number of columns 
                           # values changing acc. to outer loop
    for j in range(0, i+1): 
        # printing stars 
        print("* ",end="") 
       
        # ending line after each row 
    print("\n") 
  
input("PRESS ENTER TO EXIT")
