"""My Integration project that shows my understanding of
# COP 1500 My program will calculate your total
# meal cost based on an inputted tax and tip percentage.
# More than likely I am going to incorporate a Budgeting
# portion of the program in my Sprint 2."""
__author__ = 'Joseph Serrano'


def main():
    """The main function for the program"""
    countdown = 3
    for count in (range(1, countdown + 1)):
        print(count)
    print('Ready!')
    print("Welcome to my first ever Integration Project!")

    name = input('Hello, please enter your name: ')

    print('Good to see you,', name + '!')

    if_state = input(
        'Please enter yes if you are interested in some'
        ' basic information about the app or no if you are not!: ')
    if if_state == 'no' or if_state == 'No' or if_state == 'NO':
        print('Okay, lets get started with some simple calculations')
    elif if_state == 'yes' or if_state == 'Yes' or if_state == 'YES':
        print(
            name + ', these are just some of the basic '
                   'operations I will be using: ')
        # *-Multiplication
        print('12*8 =', 12 * 8)
        # %-Modulus
        print('17%4 =', 17 % 4)
        # /-Division
        print('9/3=', 9 / 3)
        # +-addition
        print('12+10 =', 12 + 10)
        # //-Divides and returns an integer instead of a float
        print('11//3=', 11 // 3)
        # --Subtraction
        print('11-3 =', 11 - 3)
        print(
            name + ', these are the string operators I learned within this '
                   'class and what they do: ')
        # +-concatenates
        print(
            'The + sign concatenates or joins strings such as names like '
            'this: ' + name + ', I hope your day is going '
                              'good today')
        # *-Essentially returns a string the amount of times the user * by
        print(
            'the * returns a string or variable that amount of times like '
            'this: ' + name * 10)

    continue_program = True

    while continue_program:

        option_select = input(
            'If you would like to calculate the total for a meal, type meal, '
            'or if you would like to budget, '
            'type budget: ')

        if option_select == 'meal' or option_select == 'Meal':
            # Meal price Calculator portion of app

            # Get the meal price
            meal_price = good_input = False
            while not good_input:
                try:
                    meal_price = float(
                        input("First, enter the total price of your meal: $"))
                    good_input = True
                except ValueError:
                    print("That was not a valid input, please try again.")
            # Get tax percentage
            tax_percentage = good_input = False
            while not good_input:
                try:
                    tax_percentage = float(input(
                        "Next, enter your local sales tax percentage(i.e. "
                        ".06): %"))
                    good_input = True
                except ValueError:
                    print("That was not a valid input, please try again.")
                else:
                    print(tax_percentage)
            # Get the tip percentage
            tip_percentage = good_input = False
            while not good_input:
                try:
                    tip_percentage = float(input(
                        "Finally, enter your desired tip percentage(i.e. "
                        ".15, .18, or .2): %"))
                    good_input = True
                except ValueError:
                    print("That was not a valid input, please try again.")

            # Calculate the total without the tip
            # by doing mealPrice multiplied(*) by taxPercentage
            total_without_tip = float(meal_price * tax_percentage)

            # Calculate the totalWithout tax
            # Multiply(*) mealPrice by tip percentage
            total_without_tax = float(meal_price * tip_percentage)

            # Give total for Meal By adding(+) together the
            # total_Without_tip, total_Without_tax+mealPrice
            total = (float(total_without_tip + total_without_tax + meal_price))

            print(name + ', the total cost of your meal is: $' + format(total,
                                                                        '.2f'))

            # Ask if finished or help with budgeting is needed

            test_variable: str = input(
                'Do you also need help budgeting your finances? If so, '
                'please type yes, if not type no!: ')
            if test_variable == 'no' or test_variable == 'NO' or \
                    test_variable == 'No':
                print('Okay, ' + name + ', have an amazing rest of your day!')
                continue_program = False
            elif test_variable == 'yes' or test_variable == 'YEs' or \
                    test_variable == 'YES':
                option_select = 'budget'
            else:
                print('That is an invalid input. Please try again.')
            # Budgeting portion of app

        if 'budget' == option_select or 'Budget' == option_select:
            print('Okay ' + name + ', lets get you started saving the right '
                                   'way!')

            # Get the user's monthly income

            print(
                'The next series of questions will be within the time frame '
                'of a monthly basis')

            monthly_income = good_input = False
            while not good_input:
                try:
                    monthly_income = float(
                        input('Start by entering your monthly income: $'))
                    good_input = True
                except ValueError:
                    print("That was not a valid input, please try again.")
            # Get disposable Income
            disposable_income = good_input = False
            while not good_input:
                try:
                    disposable_income = float(
                        input(
                            'Next, do you make any extra money on the side?('
                            'i.e. disposable income): $'))
                    good_input = True
                except ValueError:
                    print("That was not a valid input, please try again.")
            # Get Rent and utilities
            rent_and_utilities = good_input = False
            while not good_input:
                try:
                    rent_and_utilities = float(input(
                        'Now, we can calculate your total estimated income '
                        'to plan your budget sheet. Thirdly, '
                        'please enter your total of '
                        'your rent and utilities: $'))
                    good_input = True
                except ValueError:
                    print("That was not a valid input, please try again.")

            # Get Monthly Excess Spending
            monthly_excess_spending = good_input = False
            while not good_input:
                try:
                    monthly_excess_spending = float(
                        input(
                            'How much money do you spend on yourself?(i.e. '
                            'eating out, shopping, gas): $'))
                    good_input = True
                except ValueError:
                    print("That was not a valid input, please try again.")

            # Get estimated amount spent on groceries per month
            monthly_grocery_cost = good_input = False
            while not good_input:
                try:
                    monthly_grocery_cost = float(
                        input(
                            'Finally, about how much would you say that you '
                            'spend on groceries each month?: $'))
                    good_input = True
                except ValueError:
                    print("That is not a valid input, please try again.")

            # Calculate expenses
            expenses = float(
                rent_and_utilities + monthly_excess_spending +
                monthly_grocery_cost)

            # Calculate Income
            income = float(monthly_income + disposable_income)

            # Calculate Amount Budgeted
            amount_budgeted = float(income - expenses)

            if expenses > income or amount_budgeted < 0:

                print(name + ', You need to start saving: $',
                      format(-amount_budgeted, '.2f'))

            elif expenses < income or amount_budgeted > 0:

                print(
                    name + ', You are doing great with your money, you '
                           'appear to have an extra: $',
                    format(amount_budgeted, '.2f'))
                p = amount_budgeted * .10
                dividend_rate = .04
                time_in_years = 3
                C_I = compound_interest(p, dividend_rate, time_in_years)
                print(
                    "If you put just 10% of this extra money into a normal "
                    "dividend yield account, "
                    "you'll make an extra ${0}".format(
                        format(C_I, '.2f')), "in 3 years")

                end_state = input(
                    name + ', are you completely finished budgeting? If so, '
                           'please enter yes now. If you would '
                           'like '
                           'to run the '
                           'program again, type no: ')
                if end_state == 'no' or end_state == 'No' or end_state == 'NO':
                    continue_program = True
                elif end_state == 'yes' or end_state == 'Yes' or \
                        end_state == 'YES':
                    print(
                        'Have an awesome rest of your day, thank you for '
                        'doing your finances the right way with '
                        'us!')
                    continue_program = False

    print('We will be seeing you again soon!')


def compound_interest(principle, rate, time):
    """This function is going to be used to calculate the compound interest
    on their budgeted amount to give them a dividend yield amount"""
    result = principle * (pow((1 + rate / 100), time))
    return result


main()
