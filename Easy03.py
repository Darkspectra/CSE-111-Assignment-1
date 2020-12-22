#Easy_03

number=int(input("Enter your marks: "))
if number>=90 and number<=100:
    print("A")
elif number>=85 and number<=89:
    print("A-")
elif number>=80 and number<=84:
    print("B+")
elif number>=75 and number<=79:
    print("B")
elif number>=70 and number<=74:
    print("B-")
elif number>=65 and number<=69:
    print("C+")
elif number>=60 and number<=64:
    print("C")
elif number>=57 and number<=59:
    print("C-")
elif number>=55 and number<=56:
    print("D+")
elif number>=52 and number<=54:
    print("D")
elif number>=50 and number<=51:
    print("D-")
else:
    print("F")