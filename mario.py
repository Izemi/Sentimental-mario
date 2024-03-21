# Define a function to get a valid positive integer input from the user
def get_int(type):
    while True:
        try:
            # Try to convert user input to an integer
            return int(input(type))
        except ValueError:
            print("Invalid input. Input a positive number")


# Prompt the user for the height of the pyramid and ensure it's a valid value
height = get_int("Height: ")
# Check if the entered height is outside the valid range (1-8) and provide feedback
while height < 1 or height > 8:
    print("Height must be between 1 and 8")
    height = get_int("Height: ")
# Print the pyramid pattern
for i in range(1, height + 1):
    print(" " * (height - i) + "#" * i)
