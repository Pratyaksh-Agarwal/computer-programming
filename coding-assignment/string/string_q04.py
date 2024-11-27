#q4
# You are given a name and a positive integer. You are required to print a greeting message using the 
# name and a number of exclamation marks equal to the given integer. For example, if the given 
# name is 'John' and the integer is 3, the output should be 'Hello, John!!!'. 


# First we need to take the name as string from user input
name = input()

# Now, we need to take an integer representing the number of exclamation marks
num = int(input())
print(f'Hello, {name}{"!" * num}')