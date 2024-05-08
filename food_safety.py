"""
This module is used to check food safety
"""

import csv

def check_food_safety(food):
    """
    Check the safety information of a certain food during pregnancy from a CSV file.

    Args:
        food (str): The food to be checked for safety.

    Returns:
        tuple: The safety information of a certain food.
    """

    while True:

        with open('food_safety_list.csv', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Food'].lower() == food.lower():
                    print(row['Safety Info'], row['Precaution'], row['Food handling'])
                    return True, row['Safety Info'], row['Precaution'], row['Food handling']

        return False, None, None, None
