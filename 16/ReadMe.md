# Coffee Machine Simulation

## Introduction

This code provides a coffee machine simulation where users can select drinks, make payments, and prepare coffee. It
utilizes the `menu`, `coffee_maker`, and `money_machine` modules to create a user-friendly interface and simulate the
necessary functionalities of a coffee machine.

## Dependencies

The following dependencies are required:

- `menu`: A module that provides a menu of available drinks.
- `MenuItem`: A class representing a drink item on the menu.
- `coffee_maker`: A module that simulates a coffee maker and checks for resource availability.
- `CoffeeMaker`: A class representing a coffee maker.
- `money_machine`: A module that simulates a money machine and handles payments.
- `MoneyMachine`: A class representing a money machine.

## Main Code

### Initialization

The code starts by initializing the following objects:

- `menu`: An instance of the `Menu` class.
- `money_machine`: An instance of the `MoneyMachine` class.
- `coffee_maker`: An instance of the `CoffeeMaker` class.

### Main Loop

The code enters a while loop that continues as long as the `is_on` flag is `True`. This loop allows the user to interact
with the coffee machine by selecting options from the menu or performing specific actions.

### Menu Selection

Within the loop, the code retrieves the available drink options from the menu using the `get_items()` method. It then
prompts the user to enter their choice and stores it in the `choice` variable.

The code checks the user's choice against two special options:

- If the choice is "off", the `is_on` flag is set to `False`, and the loop will exit, turning off the coffee machine.
- If the choice is "report", the code calls the `report()` method on both the `money_machine` and `coffee_maker`
  objects. This generates a report of the current resources and financial status.

### Drink Preparation

If the user's choice is a valid drink option, the code proceeds to prepare the selected drink. It first retrieves the
corresponding `Drink` object from the menu using the `find_drink()` method.

The code then prints the price of the selected drink using the `cost` attribute of the `Drink` object.

Next, the code checks if there are sufficient resources available to make the selected drink by calling
the `is_resource_sufficient()` method of the `CoffeeMaker` object. If there are enough resources and the user
successfully makes a payment using the `make_payment()` method of the `MoneyMachine` object, the coffee maker will
proceed to make the selected drink using the `make_coffee()` method of the `CoffeeMaker` object.
