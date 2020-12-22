num_str=input("Enter a number: \n")
num_int=int(num_str)
binary,output,main="","",""

while(num_int>=1):                # This loop convert decimal to binary
    rem=num_int%2
    binary=binary+str(rem)
    num_int=num_int//2
print(binary)
for i in binary:                         # This loop inverse the binary number
    binary=int(binary)
    res=binary%10
    output=output+str(res)
    binary=binary//10
print(output)
for i in output:                         # This loop check "1" in binary number and convert to decimal
    if i is "1":
        main=main+i
num_int=int(main,2)
print(num_int)