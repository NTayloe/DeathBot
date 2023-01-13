import json
import random
# random.randrange(3, 9) includes 3 but not 9


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


weapons = ["sword", "knife", "hammer"]

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