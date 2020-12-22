#Hard_02

num=int(input("Enter a number:"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")                     # This line is for creating spaces in front of the pyramid
    if(i==num-1):
        for k in range(0,2*i+1):
            print("*",end="")             # input=3,,,,I was waiting for "i" to be turned into (input-1) value so that i can print star without spaces
    elif (i!=num-1):
        for k in range(0,i+1):          # if user input is not equal to iteration "i",,,,then i will print star with spaces
            print("*",end=" ")
    print()
for i in range(num-1,0,-1):
    for j in range(0,num-i):
        print(end=" ")                    # This line is for creating spaces in front of the pyramid
    for j in range(0,i):
        print("*",end=" ")               # This line is for creating stars after the spaces
    print()                                   # Create a new next line for next star shape