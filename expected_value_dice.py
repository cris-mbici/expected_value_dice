import random
import math
import statistics

def dice_rolling():
  #Asks the user how many dice they would like to roll and avoids a ValueError
  while True:
    try:
      dice_number = 0
      dice_number = input("How many die would you like to roll? ")
      dice_number_calc = int(dice_number)
      if dice_number_calc > 0:
        break
      else:
        print("Please enter a valid input.")
      break
    except ValueError:
      print("Please enter a valid input.")

  #Asks the user how many faces the dice will have and avoids a ValueError
  while True:
    try:
      number_of_faces = 0
      number_of_faces = input("How many faces will your dice have? ")
      number_of_faces_calc = int(number_of_faces)
      if number_of_faces_calc > 0:
        break
      else:
        print("Please enter a valid input.")
      break

    except ValueError:
      print("Please enter a valid input.")

  #This takes our outputs after rolling n times and converts them to a list
  list_of_dice = []
  while len(list_of_dice) < dice_number_calc:
    list_of_dice.append(random.randint(1, number_of_faces_calc))
  list_of_dice.sort() #Arranges our list in ascending order for median to work well
  
  #These are some basic statistics for our rolls
  mean_value = statistics.mean(list_of_dice)
  median_value = statistics.median(list_of_dice)
  mode_value = statistics.mode(list_of_dice)
  
  #This creates our initial list of faces [0, 1, 2...] without last digit
  for x in range(len(list_of_dice)):
    expected_values = []
    expected_values.append(x)
    
    
  #This is the math behind getting the expected value
  probability = 1 / number_of_faces_calc 
  expected_value = sum(range(number_of_faces_calc))
  expected_value += number_of_faces_calc #This makes sure our list is inclusive of the last digit
  expected_value *= probability

  print(f"""
  Your outcomes are {list_of_dice}
  Your mean value is {mean_value}
  Your expected value is {expected_value}      
  Some other details about your rolls are here:
  Your median is {median_value} while your mode is {mode_value}""")

  #Gives the user the choice to end the program or keep going
  user_continue = input("Would you like to roll again? (y/n) ")
  if user_continue == "y":
    dice_rolling()
  else:
    quit()
  

dice_rolling()

