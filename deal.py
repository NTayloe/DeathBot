import json
import random
# random.randrange(3, 9) includes 3 but not 9


def kill(killer, victim):
    num = random.randrange(1, 11)
    if 1 <= num <= 5:
        return f"{killer} killed {victim} with a {random.choice(weapons)}"
    else:
        return f"{killer} failed to kill {victim}"


weapons = ["sword", "knife", "hammer"]

kill_fails = ["You're trying to kill something that isn't a valid user in this server...a bold but ineffective move.",
             "You can't kill that!",
             "You can only kill real people, not your imaginary friends.",
             "Umm, try again?",
             "Are you okay?",
             "Properly mentioning people is tricky business, isn't it?"]