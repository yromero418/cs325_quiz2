def add(a, b): 
    return a + b 

def subtract(a, b): 
    return a - b 

def mult(a,b):
    return a*b

def main(): 
    print("Simple Calculator") 
    print("1. Addition") 
    print("2. Subtraction") 
    print("3. Multiplication")

    choice = input("Choose an option (1 ,2 or 3): ") 

    if choice not in ("1", "2", "3"): 
        print("Invalid choice") 
        return 
        
    # Get numbers from the user
    num1 = float(input("Enter the first number: ")) 
    num2 = float(input("Enter the second number: ")) 
    if choice == "1": 
        result = add(num1, num2) 
        print("Result:", result) 
    elif choice == "2":
        result = subtract(num1, num2) 
        print("Result:", result)
    else: 
        result = mult(num1, num2) 
        print("Result:", result)

if __name__ == "__main__": 
    main()