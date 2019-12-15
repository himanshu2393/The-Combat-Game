'''
 DEVELOPED BY: Himanshu Sharma
 DESCRIPTION: This file is the entry point for the game
              which gives choice to the players to build
              their army and begin with the combat and as
              per the rules if any player runs out of the
              army units that player will lose.
'''

# import statements here
import os
import time
from player import Player
from army_unit import ArmyUnit


# title_screen() : displays the first screen of the game with the title
def title_screen():
    # Navigation panel for the player to begin with the game.
    header = " # The Combat Game V2.0 #"  # "'\033[04m The Combat Game \033[0m'"
    start_btn = "Begin the game (Press any key...)"
    print("\n\n\n\n\n")
    print("########################".center(100))
    print("#                      #".center(100))
    print(header.center(99))
    print("#     (EXTENDED)       #".center(100))
    print("########################".center(100))
    time.sleep(2)
    print("\n" + start_btn.center(100))
    input()
    os.system("cls")


# create_player() : initializes the player and set its properties
def create_player(player_num):
    player_name = input("Player " + str(player_num) + ": Enter your name: ")

    if player_name.isalpha():
        player = Player(player_name)
    else:
        player = Player("Player_" + player_num)

    print("\n Greetings!!! King " + player_name + ", we would like to reward you with $10 as the reward to build your army to save "
                                 "your kingdom")
    return player


# begin_war() : initializes the units of both the armies and manages the battle amongst them
def begin_war(unit1, unit2, round):
    round_num = "-------- Round-" + str(round) + " --------"
    player_display = str(unit1.unit_owner) + ": " + "   || " + "    " + str(unit2.unit_owner) + ": "
    unit_display = str(unit1.type) + " versus " + str(unit2.type)
    health_display = "Unit's Health :     [" + str(unit1.health) + "] <------> [" + str(unit2.health) + "]"

    print("\n")
    print(round_num.center(100))
    print()
    print(player_display.center(100))
    print()
    print(unit_display.center(100))
    print(health_display.center(80))
    print()
    print(" O/  --->    <---  \O".center(100))
    print("/|                  |\\".center(100))
    print("/ \                / \\".center(100))
    print()

    result = unit1.versus[unit2.type]

# health is reduced based on the battle result

    if result == -1:        # Player 2 [unit2] has advantage over Player 1 [unit1]
        unit1.health -= 3
        unit2.health -= 1

    elif result == 1:       # Player 1 [unit1] has advantage over Player 2 [unit2]
        unit2.health -= 3
        unit1.health -= 1

    else:                   # Both units of same type, both loses equal health
        unit1.health -= 2
        unit2.health -= 2

#  decides based on the health which unit wins the round

    if unit1.health > 0:
        if unit2.health > 0:
            round_winner = ArmyUnit("", "")
            round_winner = begin_war(unit1, unit2, round+0.1)
            return round_winner
        else:
            print()
            print("\n| King " + str(unit1.unit_owner) + " your " + str(unit1.type) + " wins this round |")
            return unit1
    elif unit2.health > 0:
        print("\n| King " + str(unit2.unit_owner) + " your " + str(unit2.type) + " wins this round |")
        return unit2
    else:
        print("\n| Both lose, round tie |")
    return ArmyUnit("", "")


# main() : its the main controller function which is the start of the game and manages every other function call
def main():
    title_screen()
    os.system('cls')

    # Players are spawned & selects their army units
    player1 = create_player(1)
    player1.select_units()
    os.system("cls")

    player2 = create_player(2)
    player2.select_units()
    os.system("cls")

    # creating separate army unit objects to hold the respective unit of the players in the battlefield
    unit1 = ArmyUnit("", "")
    unit2 = ArmyUnit("", "")
    round_winner = ArmyUnit("", "")
    round = 1

    # to get the units arranged in the order they were purchased
    player1.army_units.reverse()
    player2.army_units.reverse()

    # Begin the combat between player 1 vs player 2 while any player runs out of army
    while len(player1.army_units) > 0 and len(player2.army_units) > 0:

        # fetch one unit each from both the armies to send in battlefield
        if unit1 == '' or unit1.type == '':
            unit1 = player1.army_units.pop()
        if unit2 == '' or unit2.type == '':
            unit2 = player2.army_units.pop()

        # war begins and round winner is decided
        round_winner = begin_war(unit1, unit2, round)
        round += 1

        if round_winner.unit_owner == str(player1.name):
            player2 = apply_medic(player2, unit2)
            unit2 = ''
        elif round_winner.unit_owner == str(player2.name):
            player1 = apply_medic(player1, unit1)
            unit1 = ''
        else:
            # respawning unit of player 1 as per the availability of funds
            player1 = apply_medic(player1, unit1)

            # respawning unit of player 2 as per the availability of funds
            player2 = apply_medic(player2, unit2)

            unit1 = ''
            unit2 = ''

    # Deciding the winner as per their army units left
    if (unit1 == '' or unit1.type == '') and len(player1.army_units) <= 0:
        if (unit2 == '' or unit2.type == '') and len(player2.army_units) <= 0:
            war_result_msg = "The Match Ties between King " + str(player1.name) + " & King " + str(player2.name)
        else:
            war_result_msg = "Congratulations King " + str(player2.name) + " you win"
    else:
        war_result_msg = "Congratulations King " + str(player1.name) + " you win"

    print("\n")
    print(war_result_msg.center(100))

    # Current army status after war
    print("\n")
    print("King " + str(player1.name) + " your remaining army : " + str([unit.type for unit in player1.army_units]))
    print("King " + str(player2.name) + " your remaining army : " + str([unit.type for unit in player2.army_units]))


# apply_medic() : applies the medic to the unit if the player has funds remaining
def apply_medic(player, unit):

    if player.funds - unit.price >= 0:
        # medic price deducted from funds as per unit's strength
        player.funds -= unit.price
        # unit respawned
        unit = ArmyUnit(unit.type, unit.unit_owner)
        # unit joined the army again
        player.army_units.append(unit)
        print("| King " + str(player.name) + " your unit is respawning and will join the army in a while... |")
    else:
        print("| King " + str(player.name) + " Sorry!! we cannot save this unit of yours. You only have $" + str(
            player.funds) + " |")

    player.army_units.reverse()
    return player


# if name of the function is main then start the game by calling main()
if __name__ == "__main__":
    main()
