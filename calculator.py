def add(a, b): 
    return a + b 

def subtract(a, b): 
    return a - b 

def main(): 
    print("Simple Calculator") 
    print("1. Addition") 
    print("2. Subtraction") 

    choice = input("Choose an option (1 or 2): ") 

    if choice not in ("1", "2"): 
        print("Invalid choice") 
        return 
        
    # Get numbers from the user
    num1 = float(input("Enter the first number: ")) 
    num2 = float(input("Enter the second number: ")) 
    if choice == "1": 
        result = add(num1, num2) 
        print("Result:", result) 
    else: 
        result = subtract(num1, num2) 
        print("Result:", result)

if __name__ == "__main__": 
    main()