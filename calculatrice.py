# define functions
def add(a, b):
    return a + b;

def sub(a, b):
    return a - b;

def mult(a, b):
    return a * b;

def div(a, b):
    return a / b;

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

operation = input("Choose an operation(1/2/3/4):");
firstNum = input("Type the first number...");
secondNum = input("Type the second number...");

if (operation == 1 ):
    print(firstNum, "+", secondNum, "=", add(firstNum, secondNum))

elif (operation == 2):
    print(firstNum, "-", secondNum, "=", sub(firstNum, secondNum))

elif (operation == 3):
    print(firstNum, "*", secondNum, "=", mult(firstNum, secondNum))

elif (operation == 4):
    print(firstNum, "/", secondNum, "=", div(firstNum, secondNum))
else:
   print("Invalid input")
