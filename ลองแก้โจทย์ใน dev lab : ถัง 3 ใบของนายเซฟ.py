colors = ['red', 'green', 'blue', 'black', 'white', 'pink', 'yellow', 'brown', 'orange']

# Get user inputs for each set
b1 = []
while len(b1) < 1:
    print("Enter at least one color for b1.")
    b1 = [input(f"Enter color {i+1}: ") for i in range(9)]

b2 = []
while len(b2) < 1:
    try:
        print("Enter at least one color for b2.")
        b2 = [input(f"Enter color {i+1}: ") for i in range(9)]
    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (e.g., user presses Ctrl+C)
        print("\nInput interrupted. Please try again.")

b3 = []
while len(b3) < 1:
    try:
        print("Enter at least one color for b3.")
        b3 = [input(f"Enter color {i+1}: ") for i in range(9)]
    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (e.g., user presses Ctrl+C)
        print("\nInput interrupted. Please try again.")

# Check if there is any common color between two out of the three sets
common_colors = set(b1) & set(b2) | set(b2) & set(b3) | set(b3) & set(b1)

# Print the resulting common colors or "none" if no common colors are found
if common_colors:
    print("Common colors:", list(common_colors))
else:
    print("None")
