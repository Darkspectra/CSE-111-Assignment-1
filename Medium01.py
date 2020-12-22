#Medium_01

'''input_num=int(input("Enter a number:"))
num1=1
num2=0
while num2<=input_num:
    print(num2,end=" ")
    num1,num2=num2,num1+num2'''

'''num1=0
num2=1
input_num=int(input("Enter a number:"))
print(num1,num2,end=" ")
for i in range(input_num):
    m=num1+num2
    if m<=input_num:
        print(m,end=" ")
    num1=num2
    num2=m'''
    

def fibonacci(n): 
    a = 0
    b = 1
    print(a,b,end=" ")
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
            print(b,end=" ") 
  
# Driver Program 
fibonacci(9)
#print(fibonacci(5)) 