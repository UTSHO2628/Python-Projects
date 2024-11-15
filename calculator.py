def calculator():
    A = input("Enter a mathematical expression: ")
    try:
        r = eval(A)
        print(f"The result is: {r}")
    except Exception as e:
        print(f"Error: {e}")

calculator()