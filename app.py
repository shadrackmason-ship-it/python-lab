# VARIABLES
student_name = "Mason"
age = 20
score = 78

print("Student Name:", student_name)
print("Age:", age)
print("Score:", score)

# ARITHMETIC OPERATORS
a = 10
b = 5

print("\nArithmetic Operators")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# COMPARISON OPERATORS
print("\nComparison Operators")
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# LOGICAL OPERATORS
x = True
y = False

print("\nLogical Operators")
print(x and y)
print(x or y)
print(not x)

# CONTROL FLOW
print("\nGrade Check")

if score >= 80:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Fail")

# EVEN OR ODD
number = 8

print("\nEven or Odd")

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# POSITIVE OR NEGATIVE
num = -5

print("\nPositive or Negative")

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# PASSWORD CHECK
password = "python123"

print("\nPassword Check")

if password == "python123":
    print("Access Granted")
else:
    print("Wrong Password")