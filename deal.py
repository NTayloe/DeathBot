import json
import random


def rr(user):
    num = random.randrange(1, 7)  # includes 1 but not 7
    if num == 3:
        return f"{user} aims a revolver with a single round in the cylinder at their head and pulls the trigger. " \
               f"They forgot to spin the cylinder before shooting, so the gun goes off and they die immediately."
    else:
        return f"{user} puts a cartridge in the cylinder of their revolver, spins it, pulls the trigger, " \
               f"and doesn't blow their head off."


def kill(killer, victim):
    num = random.randrange(1, 11)
    if 1 <= num <= 5:
        return f"{killer} killed {victim} with a {random.choice(weapons)}"
    else:
        return f"{killer} failed to kill {victim}"


def revive(reviver, revivee):
    num = random.randrange(1, 11)
    if reviver != revivee:
        if 1 <= num <= 8:
            return f"How kind of you to revive someone else! {revivee} has been brought back from the dead."
        else:
            return f"You made a noble attempt but {revivee} is just too dead to revive at this time..."
    else:
        if 1 <= num <= 5:
            return f"{reviver}'s ghost returns to their body, ready to die another day (or, more likely, later today)."
        else:
            return f"{reviver} tried to use a miracle needle, but missed the vein and revived a nearby plant instead."


# WEAPONS AND ITEMS
weapons = ["sword", "knife", "hammer", "toothpick", "battleaxe", "n arrow", "machine gun", "rocket launcher"]
weapons_weird = ["n electric toothbrush", "n orange", ""]

# FAILED COMMAND MESSAGES
rr_fails = ["You're doing it all wrong!",
            "You don't need an argument, doofus.",
            "You've clearly never played Russian Roulette before.."]
kill_fails = ["You're trying to kill something that isn't a valid user in this server...a bold but ineffective move.",
              "You can't kill that!",
              "You can only kill real people, not your imaginary friends.",
              "Umm, try again?",
              "Are you okay?",
              "Properly mentioning people is tricky business, isn't it?"]

revive_fails = ["You are trying to revive someone that doesn't exist? Interesting plan...",
                "That's not how you revive, you fool!",
                "Go ahead and take another stab at that.",
                "Are you having a stroke?"]
