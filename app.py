def main():
    operation = input("Enter + or -: ").strip()
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    print(f"Result: {result}")


main()
