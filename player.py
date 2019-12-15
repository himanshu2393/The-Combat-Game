'''
 NAME: Himanshu Sharma
 STUDENT ID: 29857082
 START_DATE: 13th AUG 2018
 END_DATE:  AUG 2018
 DESCRIPTION: This file represents the entity player who has funds, army units & a name as its properties.
              Player can select units while he has funds remaining.
'''

# import statements here
from army_unit import ArmyUnit
import time

class Player:
    funds = 0
    army_units = []
    name = ''

    # this method creates the class object.
    def __init__(self, name):
        self.funds = 10
        self.army_units = []
        self.name = name

    # this method allows player to select army units as per the menu shown.
    def select_units(self):
        unit_dict = dict({"A": "Archer", "K": "Knight", "S": "Soldier"})
        player_name = " ------ " + str(self.name) + " ------"

        while self.funds > 0:
            temp_list = []
            print("\n")
            print(player_name.center(100))
            print("Build your Army ".center(50) + "[Press 'E' to quit the game]".rjust(40))
            print("\n")
            print("".center(17) + "Current army units: " + str([unit.type for unit in self.army_units]) + " Amount: $".rjust(40) + str(self.funds))
            print("             ____________________________________________________".center(95))
            print(" <press 'A'> | Archer ".center(50) + " | PRICE: $1  |  HEALTH: [1] | ")
            print("            |_______________________|____________|______________|".center(95))
            print(" <press 'K'> | Knight ".center(50) + " | PRICE: $3  |  HEALTH: [3] |")
            print("            |_______________________|____________|______________|".center(95))
            print(" <press 'S'> | Soldier".center(50) + " | PRICE: $2  |  HEALTH: [2] |")
            print("            |_______________________|____________|______________|".center(95))

            print()
            print("['PRESS 'J' TO JOIN THE COMBAT']".center(100))
            print()

            input_msg = " UNIT SELECTIONS HERE (separated by ' ' [1 space]) : "
            temp_list = input(input_msg.center(73)).split(" ")
            if temp_list.__contains__('E'):
                exit_input = input("Are you sure you want to exit y/n ?")
                if exit_input == 'y' or exit_input == 'Y':
                    exit(0)
                else:
                    continue
            elif temp_list.__contains__('J'):
                i = 0
                while i < temp_list.index('J'):
                    if self.funds > 0:
                        unit = ArmyUnit(unit_dict[temp_list[i]], self.name)
                        if self.funds - unit.price >=0:
                            self.army_units.append(unit)  # append the army units till the 'J' choice
                            self.funds -= unit.price
                        else:
                            break
                    else:
                        break
                    i += 1

                if i < temp_list.index('J'):
                    print("\nSorry but due to your insufficient funds we could add only some units in your army")

                print("\nThis is your Army " + str([unit.type for unit in self.army_units]))
                print()
                if self.funds > 0:
                    join_combat_input = input("Are you ready to join the combat (y/n) ?")
                    if join_combat_input == 'y' or join_combat_input == 'Y':
                        break;
                    else:
                        continue
                else:
                    print("\nYou are out of funds, you cannot purchase any further units.")
                    print("Joining you in the combat")

            else:
                for elem in temp_list:
                    if elem == 'A' or elem == 'K' or elem == 'S':
                        unit = ArmyUnit(unit_dict[elem], self.name)
                        if self.funds - unit.price >= 0:
                            self.army_units.append(unit)
                            self.funds -= unit.price
                        else:
                            print("\nSorry !! insufficient funds to add few units.")
                            print("\nThis is your Army " + str([unit.type for unit in self.army_units]))
                            print("\n You can select any another unit with less buying price")
                    else:
                        print("Wrong choice selected... continue again")
                        break

            print("-------------------------------------------------------------------------- \n")
            # clear screen

        if self.funds >= 0:
            print("Joining you in the combat ... ")
            time.sleep(3)


