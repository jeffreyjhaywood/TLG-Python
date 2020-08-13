#!/usr/bin/env python3

def hasNumberAdv():
    choice = input("Does your team have more players grouped than the enemy team?\n1. Yes\n2. No\n\nType q to quit.\n")

    while not choiceCheck(choice):
        if choice == "1" or choice == "yes":
            return haveStun()
        else:
            return isTeamComing()


def haveStun():
    choice = input("Do you have a stun?\n1. Yes\n2. No\n\nType q to quit.\n")

    while not choiceCheck(choice):
        if choice == "1" or choice == "yes":
            return stunSquishy()
        else:
            return areYouSquishy()


def areYouSquishy():
    choice = input("Are you squishy? (ADC)\n1. Yes\n2. No\n\nType q to quit.\n")

    while not choiceCheck(choice):
        if choice == "1" or choice == "yes":
            return print("Wait for your team to engage.")
        else:
            return print("Engage when your team is ready.")


def stunSquishy():
    return print("Stun the enemy team's carry and shred everyone apart!")


def isTeamComing():
    choice = input("Is your team on their way?\n1. Yes\n2. No\n\nType q to quit.\n")

    while not choiceCheck(choice):
        if choice == "1" or choice == "yes":
            return poke()
        else:
            return inJeffPromos()


def poke():
    print("Poke from distance until fair fight.")


def inJeffPromos():
    choice = input("Are you in Jeffrey's promos?\n1. Yes\n2. No\n\nType q to quit.\n")

    while not choiceCheck(choice):
        if choice == "1" or choice == "yes":
            return backOff()
        else:
            return oneVsFive()


def backOff():
    print("Back off, and poke from a safe distance. Be careful not to get caught out.")


def oneVsFive():
    print("1 v 5 the enemy team. 0/12 is just a number, you got this.")


def choiceCheck(choice):
    if choice == "q":
        print("Exiting script.")
        exit()
    if choice != "1" or choice != "yes" or choice != "2" or choice != "no":
        return False
    else:
        return True

def main():
    print("League of Legends team fight engagement flowchart")
    print("========================================")

    hasNumberAdv()

while True:
    main()
