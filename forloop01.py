x=0
for i in range (1,11):
    square = i**2
    if square % 4 == 0:
        x += square
        
print("sum of squares divisible by 4 from 1 to 10 is:",x)    