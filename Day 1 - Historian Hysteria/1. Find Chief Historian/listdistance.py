# Initialise Empty Lists
left_list = []
right_list = []

# Read file contents 
with open('input.txt', 'r') as file:
    puzzle_input = file.read()

# Do the following for each new line
for line in puzzle_input.strip().split("\n"):
    left, right = map(int, line.split()) # Split each line into two integers
    left_list.append(left)
    right_list.append(right)


# Sort lists - ascending order
left_sorted = sorted(left_list)
right_sorted = sorted(right_list)


# Calculate distance between each pair 
total_distance = sum(abs(left_sorted[i]-right_sorted[i]) for i in range(len(left_sorted)))

# Print distance
print(total_distance)

