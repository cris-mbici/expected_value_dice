from collections import Counter
import random
import math
import statistics
from tabulate import tabulate

#Our main dice rolling function
def dice_rolling():
    while True:
        try: #Ensures user input is valid, asks number of dice to be rolled
            dice_number = int(input("How many die would you like to roll? "))
            if dice_number > 0:
                break
            print("Please enter a valid input.")
        except ValueError:
            print("Please enter a valid input.")

    while True: #Ensures user input is valid, asks number of faces in dice
        try:
            number_of_faces = int(input("How many faces will your dice have? ").strip())
            if number_of_faces > 0:
                break
            print("Please enter a valid input.")
        except ValueError:
            print("Please enter a valid input.")

    # Generate and sort dice rolls
    list_of_dice = sorted(random.randint(1, number_of_faces) for _ in range(dice_number))

    # Basic statistics calculations
    mean_value = statistics.mean(list_of_dice)
    median_value = statistics.median(list_of_dice)
    mode_value = statistics.mode(list_of_dice)

    # Expected value calculations
    probability = 1 / number_of_faces
    expected_value = sum(range(1, number_of_faces + 1)) * probability

    # Standard deviation calculations
    modified_list = [(x - mean_value) ** 2 for x in list_of_dice]
    standard_deviation = math.sqrt(sum(modified_list) / len(modified_list))

    # Table data for unique values and their counts
    counts = Counter(list_of_dice)
    data = [[num, count] for num, count in counts.items()]

    # Final output
    print(f"""
Your outcomes are:
{tabulate(data, headers=["Number", "Occurrence"], tablefmt="grid")}
Your mean value is {mean_value:.4g}
Your expected value is {expected_value:.4g}      
Your median is {median_value} while your mode is {mode_value:.4g}
Your standard deviation is {standard_deviation:.4g}
""")

    # Final prompt to ask user if they'd like to roll again
    user_continue = input("Would you like to roll again? (y/n) ")
    if user_continue.lower() == "y":
        dice_rolling()
    else:
        print("Thanks for playing!")
        quit()

dice_rolling()
