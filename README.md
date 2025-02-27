# 🎲 Dice Rolling Simulator

This Python script is a simple yet effective way to simulate rolling dice with customizable settings.

You start by choosing how many dice you want to roll and how many faces each die should have. Once rolled, the program generates a list of sorted results and calculates key stats, 
including the mean, median, mode, and expected value. The expected value is determined using probability calculations, giving insight into the theoretical average outcome.

One of the best features is the option to keep rolling—after each round, you can decide whether to roll again or exit the program. 
Everything runs on Python’s built-in modules (`random`, `math`, and `statistics`), so no additional installations are required.

To get started, simply run:
```
python dice_rolling.py
```
Follow the prompts, enter your preferred settings, and see the results. If you roll multiple times, you can start noticing patterns and trends in your dice rolls. 

A sample output might look like this:
```
Your outcomes: [2, 4, 6]
Mean: 4.0, Expected: 3.5
Median: 4.0, Mode: 2
Roll again? (y/n)
```

A couple of things to note—currently, the program assumes there’s always a mode in the results, which might cause an error if all dice rolls are unique. 
Also, the expected value calculation doesn’t account for repeated numbers when rolling multiple dice, something that could be refined in future updates.
Future improvements could include adding better handling for cases with no mode, 
supporting weighted dice for more advanced probability simulations, and even incorporating a graphical representation of results for better visualization.

[Watch the demo](https://github.com/cris-mbici/expected_value_dice/raw/main/dice_roller.mp4)

