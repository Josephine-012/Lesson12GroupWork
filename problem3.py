def is_even(number) :
    return number % 2 == 0
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_even(num):
        print("True")
    else:
        print("False")
