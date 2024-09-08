#To find roots of quadratic equation
print("Given Quad Eq: ax^2 + bx + c = 0")
a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))
c = float(input("Enter the value for c: "))
D = (b*b) - (4*a*c)
comp = False
x1,x2 = 0,0
xc1,xc2 = "",""
if a == 0:
    if b == 0:
        print("No solution")
    else:
        print("The solution for x is =",(-1*c/b))

else:
    if D < 0:
        D = -1*D
        comp = True

    if not comp:
        x1 = ((-1*b + D**0.5)/(2*a))
        x2 = ((-1*b - D**0.5)/(2*a))
        print("The solutions for x are = ",x1," and ",x2)

    else:
        xc1 = str((-1*b)/(2*a)) + " + " + str(D**0.5/(2*a)) + "i"
        xc2 = str((-1*b)/(2*a)) + " - " + str(D**0.5/(2*a)) + "i"
        print("The solutions for x are = ",xc1," and ",xc2)


'''
OUTPUT

Given Quad Eq: ax^2 + bx + c = 0
Enter the value for a: 6
Enter the value for b: 3
Enter the value for c: 8
The solutions for x are =  -0.25 + 1.1273124382057236i  and  -0.25 - 1.1273124382057236i
'''


