def expo(x,y):
    for i in range(y-1):
        x=x*x
        print(x)
    return x
x=10
y=3
print(f"{x} raised to {y} is {expo(x,y)}") 
