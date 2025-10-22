# Understand:
# Make code that takes a number as input and outputs an array
# The array is as long as the inputted number
# Go through each number until you reach inputted number, and put something specific in the array corresponding to each number

# Clues:
# The program goes through each number until you reach the inputted number
# This normally means you use a for loop

# Assemble:
# n = input
# answer = empty list
# for i less than n:
# if i + 1 is divisible by 3 and i + 1 is divisible by 5:
# add "FizzBuzz" to answer
# else if i + 1 is divisible by 3:
# add "Fizz" to answer
# else if i + 1 is divisible by 5:
# add "Buzz" to answer
# else:
# add i to answer
# output answer

# Solve:
n = int(input("Input: n = "))
answer = []
for i in range(n):
    if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
        answer.append("FizzBuzz")
    elif (i + 1) % 3 == 0:
        answer.append("Fizz")
    elif (i + 1) % 5 == 0:
        answer.append("Buzz")
    else:
        answer.append(i + 1)
print(f"Output: {answer}")

# Evaluate:
# The code works, but it would have been more readable if I did 2 things
# It would have been better if I did for i in range(n + 1) instead of putting i + 1 everywhere
# It would have been better if there was a .divisible function or if I made one