"""This page is for individual treasure payout for small things
    utilizing the Dungeon Master for majority of the treasures with some added spunk"""

dice_roll = 0


class Challenge04:
    if dice_roll <= 1 and dice_roll <= 30:
        copper = '5d6'
    elif dice_roll <= 31 and dice_roll <= 60:
        silver = '4d6'
    elif dice_roll <= 61 and dice_roll <= 70:
        gold = '4d6'
    elif dice_roll <= 71 and dice_roll <= 95:
        gold = '8d6'
    elif dice_roll <= 96 and dice_roll <= 100:
        platinum = '3d6'


class Challenge510:
    if dice_roll <= 1 and dice_roll <= 30:
        copper = '4d6'
    elif dice_roll <= 31 and dice_roll <= 60:
        silver = '4d6'
    elif dice_roll <= 61 and dice_roll <= 70:
        gold = '4d6'
    elif dice_roll <= 71 and dice_roll <= 95:
        gold = '8d6'
    elif dice_roll <= 96 and dice_roll <= 100:
        platinum = '3d6'


class Challenge1116:
    if dice_roll <= 1 and dice_roll <= 20:
        silver = '4d6'
        gold = '1d6'
    elif dice_roll <= 21 and dice_roll <= 35:
        gold = '3d6'
    elif dice_roll <= 36 and dice_roll <= 75:
        gold = '2d6'
        platinum = '3d6'
    elif dice_roll <= 76 and dice_roll <= 100:
        gold = '3d6'
        platinum = '4d6'


class Challenge17:
    if dice_roll <= 1 and dice_roll <= 15:
        gold = '10d6'
    elif dice_roll <= 16 and dice_roll <= 55:
        gold = '3d6'
        platinum = '3d6'
    elif dice_roll <= 56 and dice_roll <= 100:
        gold = '6d6'
        platinum = '6d6'
