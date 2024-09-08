#Making a python calculator with dynamic options

print("----------------------------------------")
print("           PYTHON CALCULATOR")
print("----------------------------------------")
num = 0
temp_num = 0
total = 0
op = ""
display = ""
temp_display = ""
num_string = ""
num = float(input("Enter number: "))
total = num
num_string = str(num)
while True:
    op = input("Enter the operator (+,-,*,/,=): ")
    if op == "=":
        break
    temp_num = float(input("Enter number: "))
    print("\n")
    if op == "+":
        total += temp_num
        num_string = num_string + " + " + str(temp_num)
        print(num_string)
        print("\n")
    elif op == "-":
        total -= temp_num
        num_string = num_string + " - " + str(temp_num)
        print(num_string)
        print("\n")
    elif op == "*":
        total *= temp_num
        num_string = num_string + " * " + str(temp_num)
        print(num_string)
        print("\n")
    elif op == "/":
        total /= temp_num
        num_string = num_string + " / " + str(temp_num)
        print(num_string)
        print("\n")
print(num_string,"=",total)

'''
OUTPUT

Enter number: 323.32
Enter the operator (+,-,*,/,=): -
Enter number: 324


323.32 - 324.0


Enter the operator (+,-,*,/,=): +
Enter number: 5.2


323.32 - 324.0 + 5.2


Enter the operator (+,-,*,/,=): /
Enter number: 4324


323.32 - 324.0 + 5.2 / 4324.0


Enter the operator (+,-,*,/,=): =
323.32 - 324.0 + 5.2 / 4324.0 = 0.0010453283996299707
'''
        
    
