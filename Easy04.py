#Easy_04

num=int(input("Enter a number: "))
x=0
for i in range(1,num+1):
    if num%i==0:
        x+=1
if x==2:
    print(num,"is prime")
else:
    print("Not prime number")
    
# Another Way_
'''S = int(input())
if S > 1:
    for i in range(2,S):
        if S%i==0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not prime")'''