import math

def solve(a, b, c):
    d = b ** 2 - 4 * a * c 
    roots = []

    if d < 0: 
        roots = ["There are no", "real roots"]
    else:
        roots = [round((-b + math.sqrt(d)) / 2 * a, 2), round((-b - math.sqrt(d)) / 2 * a, 2)] 

    return roots

print("Enter the coefficients for ax^2 + bx + c = 0") 
a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

print(solve(a,b,c)[0], solve(a,b,c)[1]) 