def Fibo(n):

    if n < 0:
        print("Incorrect Input")

    # First Fibonacci Number is 0
    elif n == 1:
        return 0

    # First Fibonacci Number is 1
    elif n == 2:
        return 1

    # Recurssion for Others
    else:
        return Fibo(n-1) + Fibo(n-2)
