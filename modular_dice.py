import random
import math
import statistics
import matplotlib.pyplot as plt
from collections import Counter
from tabulate import tabulate  # This just makes the output look cleaner

# Get user input for number of dice and faces
# Keep asking until they give valid numbers
def get_user_input():
    while True:
        try:
            dice_number = int(input("How many dice would you like to roll? "))
            if dice_number > 0:
                break  # Valid input, move on
            print("Please enter a valid number of dice.")
        except ValueError:
            print("Please enter a valid input.")  # They typed something weird

    while True:
        try:
            number_of_faces = int(input("How many faces will your dice have? ").strip())
            if number_of_faces > 0:
                break  # Again, move on when valid
            print("Please enter a valid number of faces.")
        except ValueError:
            print("Please enter a valid input.")  # Another bad input case

    return dice_number, number_of_faces

# Rolls the dice and returns a sorted list of results
def roll_dice(dice_number, number_of_faces):
    return sorted(random.randint(1, number_of_faces) for _ in range(dice_number))

# Does all the math for the dice rolls, so we don’t have to think
def calculate_statistics(dice_rolls, number_of_faces):
    mean_value = statistics.mean(dice_rolls)
    median_value = statistics.median(dice_rolls)
    mode_value = statistics.mode(dice_rolls)  # This fails if all values are unique, but let's assume normal dice rolling

    probability = 1 / number_of_faces  # Probability of rolling any single face
    expected_value = sum(range(1, number_of_faces + 1)) * probability  # Theoretical mean

    # Calculate standard deviation manually (just for fun, stats library also has this)
    modified_list = [(x - mean_value) ** 2 for x in dice_rolls]
    standard_deviation = math.sqrt(sum(modified_list) / len(modified_list))

    return mean_value, median_value, mode_value, expected_value, standard_deviation

# Makes a frequency graph (kinda) using a dictionary
def generate_graph_data(dice_rolls):
    return dict(Counter(dice_rolls))  # Counts how many times each number shows up

# We're using the graphing module,again sorry for 1000 comments here, this is my learning template
def plot_graph(graph_data): 
    number = list(graph_data.keys()) # Convert the dictionary keys (dice roll outcomes) into a list  
    counts = list(graph_data.values()) # Convert the dictionary values (how many times each outcome appeared) into a list

    plt.bar(numbers, counts, color="skyblue") # Create a bar chart where the x-axis is the dice roll results and the y-axis is how often they appeared
    plt.xlabel("Dice Roll Outcome") # Label the x-axis so we know what the numbers represent
    plt.ylabel("Occurrences") # Label the y-axis so we know what the height of each bar means  
    plt.title("Dice Roll Distribution") # Add a title so it looks neater
    # Add a light grid in the background to make it easier to read values  
    plt.grid(axis="y", linestyle="--", alpha=0.5) # Dashed lines, slightly transparent
    plt.show() # Actually show the graph (otherwise it won't appear)  

# Prints everything nicely (well, as nicely as the terminal allows)
def display_results(dice_rolls, stats, graph_data):
    mean_value, median_value, mode_value, expected_value, standard_deviation = stats

    data = [[num, count] for num, count in graph_data.items()]

    print(f"""
Your outcomes are:
{tabulate(data, headers=["Number", "Occurrence"], tablefmt="grid")}
Your mean value is {mean_value:.4g}
Your expected value is {expected_value:.4g}      
Your median is {median_value} while your mode is {mode_value:.4g}
Your standard deviation is {standard_deviation:.4g}
""")

# Main function that runs everything
def dice_rolling():
    dice_number, number_of_faces = get_user_input()
    dice_rolls = roll_dice(dice_number, number_of_faces)
    stats = calculate_statistics(dice_rolls, number_of_faces)
    graph_data = generate_graph_data(dice_rolls)
    display_results(dice_rolls, stats, graph_data)

    # Ask if they wanna go again
    user_continue = input("Would you like to roll again? (y/n) ").strip().lower()
    if user_continue == "y":
        dice_rolling()  # Recursion! Feels fancy
    else:
        print("Thanks for playing!")
        quit()

# Let’s get rolling!
dice_rolling()
