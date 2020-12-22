#Hard_01

num=int(input("Enter number:"))
count,count1,store=0,0,0
while(num>0):
    x=num%10
    if(store==x):
        count1+=1
    store=x
    count+=1
    num=num//10
print(count-count1)