#Hard_03

num=int(input("Enter a number: \n"))
binary=int(bin(num)[2:])
count=0
print(binary)
while (binary>=1):
    if binary%2==1:
         count+=1
         binary=binary//10
    else:
        binary=binary//10
z=1
for i in range(1,count):
    z=10**i+z
x=str(z)
a=int(x,2)
print(a)