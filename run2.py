from food_items import *
from order import Order
from people import *
from run_very_nice import *
from general_functions import *
# Want a game to keep running
# Want following
    # as user create customer
    # as user create food item
    # as user can list food items
    # as user I can create orders
    # as user I can add items to order
    # as user I can see the total of an order
help = '    Please type EXIT to leave the terminal \n    Please type "1" to input customer \n    Please type "2.1" to input a menu item \n    Please type "2.2" to remove a menu item \n    Please type "3" to start an order \n    Please type HELP for this help again'
print(help)

while True:
    # get user input for print option
    user_input = input('Where would you like to go?:   ')
    if user_input.upper() == 'EXIT':
        print('Goodbye')
        break
    elif user_input.upper() == 'HELP':
        print(help)
    elif user_input == '1':
        print("You've added a customer")
    elif user_input == '2.1':
        print("You've added a menu item")
    elif user_input == '2.2':
        secondary_input = input('Which menu item do you wish to remove? \n(Type "N" to return to the options screen):   ')
        if secondary_input.upper() == 'N':
            pass
        else:
            print('You have removed {Jason} from the')
            pass
    elif user_input == '3':
        print("You've created a new order")
        print("Menu:")
        for i in FoodItems.food_items_list:
            print(f"{(vars(i)['item']).capitalize()}: {set_two_dp_price(vars(i)['price'])}")
        while True:
            input("What food items are you adding to your order: ")

    else:
        print('Unknown command, please enter code again')
# evaluate and go to each option
        # inside each option, do logic, and create what ever you need to create
