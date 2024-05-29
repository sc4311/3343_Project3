import random

PUZZLE_SIZE = 10
# Create random puzzle
# random.sample ensures no duplicates
puzzle_nums = random.sample(range(100), PUZZLE_SIZE)
puzzle_symbols = []
# Randomly assign inequalities
for i in range(PUZZLE_SIZE - 1):
    puzzle_symbols.append(">" if random.random() < .5 else "<")
print("Random puzzle numbers: ", puzzle_nums)
print("Randomly assign inequalities: ", puzzle_symbols)


# Sort puzzle numbers first
# Use the largest remaining if greater than, smallest remaining if less than
# Sort puzzle numbers in ascending order
sorted_puzzle_nums = sorted(puzzle_nums)
# Vars for the "two pointer" method
low = 0
high = PUZZLE_SIZE - 1
# store solution values
solution_values = []

for symbol in puzzle_symbols:
    if symbol == '<':
        solution_values.append(sorted_puzzle_nums[low])
        low += 1
    else:  # symbol == '>'
        solution_values.append(sorted_puzzle_nums[high])
        high -= 1
# Add the last remaining number
solution_values.append(sorted_puzzle_nums[low])

# The rest of the code remains the same


# Convert solution_values to list of strings
solution_values = list(map(str, solution_values))
# Create a list to store the final solution representation
final_solution_representation = [None] * (len(solution_values) + len(puzzle_symbols))
# Create solution representation using nifty slicing with step parameter
final_solution_representation[::2] = solution_values
final_solution_representation[1::2] = puzzle_symbols
# Display final solution
# The join() method takes all items in an iterable and joins them into one string
print("Final solution: ", " ".join(final_solution_representation))
# Evaluate whether solution is correct.
print(eval(" ".join(final_solution_representation)))
