def find_max(a,b):
    if(a>b):
        return a
    else:
        return b

num1 = int(input("Enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
num4=int(input("enter fourth number"))

max1=find_max(num1,num2)
max2=find_max(num3,num4)
print("Maximum of first two", max1)
print("Maximum of next two", max2)
