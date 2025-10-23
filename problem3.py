# U: I need to create a program that checks if the number is even or odd
# C: Ask the user to input a number and the code,
# convert the input to an integer (since input() gives us a string, 
# write function is_even(number) that checks if the number is divisible by 2,
# if the remainder is 0, return "True." Otherwise,, return "False."
# print the result to the user
# A and S:
def is_even(number) :
    return number % 2 == 0
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_even(num):
        print("True")
    else:
        print("False")
# E: This program will ask for a number. The function will check if the number has a remainder of 0 when divided by 2. If yes, it will print tru. If no, it will print false.
