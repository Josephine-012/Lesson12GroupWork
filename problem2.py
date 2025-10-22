#Find the factorial of a number
#Factorials is the product of all positive integers from one to the number (n)

#Define a funciton called factorial(n)
#if n < 0 return an error message
#If n == 0 or equals 1 then print 1
#other wise print n * factorial(n-1)
#ask for an input

def factorial(n):
    """Return the factorial of n."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    


number = int(input("Enter a number: "))
print("Factorial:", factorial(number))

