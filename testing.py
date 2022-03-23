import random
from DnD_Treasure.dice_roll_fundamentals.random_dice_roll import random_gem_roll


def all_random_roll(*args):
    print("Hello World")
    print(args)


def testing_function(**kwargs):
    copper = kwargs.get("copper")
    copper_multiplier = kwargs.get("copper_multiplier")
    silver = kwargs.get("silver")
    silver_multiplier = kwargs.get("silver_multiplier")
    copper_sum_roll = 0
    final_copper = 0
    silver_sum_roll = 0
    final_silver = 0
    if kwargs.get("copper"):
        for i in range(int(copper[0])):
            roll = random.randint(1, int(copper[2]))
            copper_sum_roll = copper_sum_roll + roll
            if copper_multiplier == 0:
                final_copper = copper_sum_roll
            else:
                final_copper = copper_sum_roll * copper_multiplier
        print("Copper:", final_copper)
    if kwargs.get("silver"):
        for i in range(int(silver[0])):
            roll = random.randint(1, int(silver[2]))
            silver_sum_roll = silver_sum_roll + roll
            if silver_multiplier == 0:
                final_silver = silver_sum_roll
            else:
                final_silver = silver_sum_roll * silver_multiplier
        print("Silver:", final_silver)


class RollRandomMoney:

    def __init__(self,
                 copper,
                 copper_multiplier,
                 silver,
                 silver_multiplier,
                 gold,
                 gold_multiplier,
                 platinum,
                 platinum_multiplier):
        self.copper = copper
        self.copper_multiplier = copper_multiplier
        self.silver = silver
        self.silver_multiplier = silver_multiplier
        self.gold = gold
        self.gold_multiplier = gold_multiplier
        self.platinum = platinum
        self.platinum_multiplier = platinum_multiplier

    def copper_roll(self):
        copper_sum_roll = 0
        final_copper = 0
        silver_sum_roll = 0
        final_silver = 0
        gold_sum_roll = 0
        final_gold = 0
        platinum_sum_roll = 0
        final_platinum = 0
        if self.copper != "":
            for i in range(int(self.copper[0])):
                roll = random.randint(1, int(self.copper[2]))
                copper_sum_roll = copper_sum_roll + roll
                if self.copper_multiplier == 0:
                    final_copper = copper_sum_roll
                else:
                    final_copper = copper_sum_roll * self.copper_multiplier
            print("Copper:", final_copper)
        if self.silver != "":
            for i in range(int(self.silver[0])):
                roll = random.randint(1, int(self.silver[2]))
                silver_sum_roll = silver_sum_roll + roll
                if self.silver_multiplier == 0:
                    final_silver = silver_sum_roll
                else:
                    final_silver = silver_sum_roll * self.silver_multiplier
            print("Silver:", final_silver)
        if self.gold != "":
            for i in range(int(self.gold[0])):
                roll = random.randint(1, int(self.gold[2]))
                gold_sum_roll = gold_sum_roll + roll
                if self.gold_multiplier == 0:
                    final_gold = gold_sum_roll
                else:
                    final_gold = gold_sum_roll * self.gold_multiplier
            print("Gold:", final_gold)
        if self.platinum != "":
            for i in range(int(self.platinum[0])):
                roll = random.randint(1, int(self.platinum[2]))
                platinum_sum_roll = platinum_sum_roll + roll
                if self.platinum_multiplier == 0:
                    final_platinum = platinum_sum_roll
                else:
                    final_platinum = platinum_sum_roll * self.platinum_multiplier
            print("Platinum:", final_platinum)


def if_else_test():
    dice_random = random.randint(1, 100)
    print(dice_random)
    if 1 <= dice_random <= 30:
        print("1 to 30")
    elif 31 <= dice_random <= 69:
        print("31 to 69")
    elif 70 <= dice_random <= 100:
        print("70 to 100")


def gem_random_roll(gem):
    gem_sum_roll = 0
    print(gem)
    for i in range(int(gem[0])):
        roll = random.randint(1, int(gem[2]))
        gem_sum_roll = gem_sum_roll + roll
    print(gem_sum_roll)
