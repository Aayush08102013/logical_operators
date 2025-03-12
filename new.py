# logical operators
a = 784
b = 67
c = 95

if (a>b) and (a>c):
    print("a is greator than, b and b")

elif (b>a) and (b>c):
    print("b is greator than, a and c")
else:
       print("c is greator than, a and b") 

# pen or pencil

p1 = "pencil" 
p2 = "pen"

if p1 or p2:
     print("i can use either one of them")

else:
     print("using any can do")

# != not equals to:
num1 = int(input("enter a number "))
num2 = 26
if (num1 != num2):
     print("the 2 numbers are diffrent")
else:
     print("the 2 numbers are the same")     
#BMI calculation
w = float(input("enter your weigth in kgs: "))
h = float(input("enter your height in cm: "))

BMI = w/(h/100)**2
print(f"your BMI is {BMI}")
if BMI <= 18.4:
     print("your under weigth")
elif BMI <= 24.9:
     print("your healthy")
elif BMI <= 29.9:
     print("your over weight")
elif BMI <= 34.9:
     print("your severly over weight")
elif BMI <= 39.9:
     print("your obese")
else:
     print("you are severly obese")
    