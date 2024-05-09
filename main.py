"""
Pregnancy Tracker Application

Term 1, Assignment 3
Web Development Accelerated Program
Coder Academy

Student/Author: John Fuentes
"""

# Import statements
import sys
from textwrap import dedent
from datetime import datetime
from print_guide import guide, instructions
from pregnancy_calculator import (
    calculate_gestational_age,
    calculate_trimester,
    calculate_due_date,
    calculate_countdown
)
from food_safety import check_food_safety
from travel_safety import check_travel_safety
from activities_safety import check_activities_safety

# Helper functions
def get_last_period_date() -> datetime.date:
    """
    Prompt user to enter the last menstrual period date and parse the input for validation.

    Returns:
        datetime.date: The parsed date object representing the last menstrual period date.

    """
    # Display the guide for instructions and for quitting the app
    guide() # From print_guide module

    while True:
        # Prompt user to enter the date of her last menstrual period
        user_input_date = input('Enter the date of your last menstrual period (DD/MM/YYYY): ')

        # Check if user want to view the instructions or exits the app
        guide_user_response(user_input_date)

        try:
            # Convert user input string into datetime.date object in DD/MM/YYYY format
            last_period_date = datetime.strptime(user_input_date, '%d/%m/%Y').date()
            return last_period_date
        except ValueError:
            # Display the guide for instructions and for quitting the app
            guide() # From print_guide module

            # Handles error gracefully if user entered invalid date format
            print('Error: You entered an invalid format. Please enter the date in DD/MM/YYYY.\n')

def get_travel_date() -> datetime.date:
    """
    Prompt user to enter the planned travel date for validation.

    Returns:
        datetime.date: The parsed date object representing the date of planned travel.
    """

    while True:
        # Prompt the user the date of her planned travel date
        user_input_date = input('Enter the date of your planned travel (DD/MM/YYYY): ')

        # Check if user want to view the instructions or exits the app
        guide_user_response(user_input_date)

        try:
            # Convert user input string into datetime.date object in DD/MM/YYYY format
            travel_date = datetime.strptime(user_input_date, '%d/%m/%Y').date()
            return travel_date
        except ValueError:
            # Handles error gracefully if user entered invalid date format
            print('Error: You entered an invalid format. Please enter the date in DD/MM/YYYY.\n')

def guide_user_response(response: str) -> None:
    """
    Check if user enters 'INSTRUCTIONS' or 'QUIT' case-insensitive

    Args:
        response (str): User can enter 'INSTRUCTIONS' or 'QUIT' at any given time
    """
    # Check if user wants to view the instructions
    if response.lower() == 'instructions':
        instructions()

    # Check if user wants to exit the app
    if response.lower() == 'quit':
        sys.exit()

def get_user_next_action() -> bool:
    """
    Prompt the user for the next action whether to continue in current sub menu, return to main menu or exit.

    Returns:
        bool: True if user chooses to continue or False if user chooses to return to main menu.
    """
    while True:
        # Prompt the user to get her response
        next_choice = input('\n\nWhat would you like to do next?\n'
                            '1. Continue\n'
                            '2. Return to main menu\n\n'
                            'Enter your choice (1 or 2): ')

        # Check if user want to view the instructions or exits the app
        guide_user_response(next_choice)

        # Check what choice the user selected
        if next_choice == '1':
            return True
        elif next_choice == '2':
            return False
        else:
            # Display the guide for instructions and for quitting the app
            guide() # From print_guide module

            # Inform the user that she entered invalid choice
            print('Invalid choice. Please enter 1, 2 or 3.\n')

# Main functions
def pregnancy_information() -> None:
    """
    Calculate and display the information about pregnancy such as gestational age 
    in weeks, trimester, estimated due date (EDD) and countdown until EDD.
    """
    while True:
        # Prompt user to enter the date of her last menstrual period
        last_period_date = get_last_period_date()

        # Calculate gestational age in weeks
        gestational_age = calculate_gestational_age(last_period_date)

        # Calculate trimester based on gestational age
        trimester = calculate_trimester(gestational_age)

        # Calculate estimated due date
        due_date = calculate_due_date(last_period_date)

        # Calculate the countdown from current date until due date
        weeks_remaining, days_remaining = calculate_countdown(due_date)

        # Display the guide for instructions and for quitting the app
        guide() # From print_guide module

        # Display relevant information about the pregnancy
        print(f'\nYou are {gestational_age} weeks pregnant.\n')
        print(f'Trimester: {trimester}')
        print(f"Estimated Due Date: {due_date.strftime('%d/%m/%Y')}")
        print(f'Due Date Countdown: {weeks_remaining} week(s) and {days_remaining} day(s)')

        # Prompt user what she wants to do next
        if not get_user_next_action():
            break # Return to main menu based on user choice

def safety_info() -> None:
    """
    Prompt user to select from the three topics related to safety in pregnancy.
    """

    # Display the guide for instructions and for quitting the app
    guide() # From print_guide module

    while True:
        # Give the user options for the topics related to safety
        print(dedent('''\nSelect a topic:\n
        1. Food Safety
        2. Travel Safety
        3. Activities Safety
        '''))

        # Prompt the user her choice
        choice = input('Enter your choice (1, 2 or 3): ')

        # Check if user want to view the instructions or exits the app
        guide_user_response(choice)

        # Check what the user entered
        if choice == '1':
            # Prompt the user what food she wants to know for the safety information
            food = input('Enter a food item: ').lower()

            # Check if user want to view the instructions or exits the app
            guide_user_response(choice)

            # Calls the function check_food_safety in food_safety module
            food_safety_info, food_precaution, food_handling = check_food_safety(food)

            # Display only if the food entered by the user has available safety information
            if food_safety_info:
                print(f'\nFood: {food.capitalize()}\n')
                print(f'Food Safety Information: {food_safety_info}')

                # Display only if the value in food_precaution is not an empty string
                if food_precaution:
                    print(f'Precaution: {food_precaution}')

                # Display only if the value in food_handling is not an empty string
                if food_handling:
                    print(f'Food Handling: {food_handling}')

            # Inform the user that the food she entered has no available safety information.
            else:
                # Display the guide for instructions and for quitting the app
                guide() # From print_guide module

                # Inform user that the food she entered has no available safety information
                print(f'Sorry, the safety information of "{food}" is not available.\n')

        elif choice == '2':
            # Prompt user the date of her last menstrual period
            last_period_date = get_last_period_date()

            # Prompt user the date of her planned travel
            travel_date = get_travel_date()

            # Obtain the travel information from travel_safety module
            travel_infos = check_travel_safety(travel_date, last_period_date)

            # Display travel safety information with indices
            for index, travel_info in enumerate(travel_infos, 1):
                # Display only if travel info is not an empty string
                if travel_info:
                    print(f'{index}. {travel_info}')

        elif choice == '3':
            check_activities_safety()
        else:
            # Inform the user that she entered an invalid choice
            print('Error: Invalid choice. Please enter 1 for Food Safety, 2 for Travel Safety or 3 for Activities Safety\n')

def note_taking():
    pass

# Execution entry point
def main() -> None:
    """
    Main function that allows the user to select from the features of pregnancy tracker app.
    """

    print('\nWelcome to Pregnancy Tracker App!\n')

    while True:
        # Display the guide for instructions and for quitting the app
        guide() # From print_guide module

        # Give user options based on the features of this app
        print(dedent('''
        Select from the following features.\n
        1. Pregnancy Information
        2. Safety Information
        3. Take Down Notes
        '''))

        # Prompt the user of her choice
        choice = input('Enter your choice (1, 2 or 3): ')

        # Check if user want to view the instructions or exits the app
        guide_user_response(choice)

        # Check what option the user selected
        if choice == '1':
            pregnancy_information()
        elif choice == '2':
            safety_info()
        elif choice == '3':
            note_taking()
        else:
            # Inform the user if she entered invalid choice
            print('Invalid choice. Please enter 1, 2 or 3.\n')

# Execute main function when the script is run
if __name__ == "__main__":
    main()
