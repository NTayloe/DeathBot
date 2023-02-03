# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import random
import discord
from discord.ext import commands
import deal

# SETUP
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True
bot = commands.Bot(
    command_prefix="!",
    case_insensitive=True,
    activity=discord.Activity(type=discord.ActivityType.watching, name="mortals die"),
    intents=intents,
)


# STARTUP
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


# ----------------------------------------------------------------------------------------------------------------------
# RUSSIAN ROULETTE
@bot.command(aliases=['roulette', 'russianroulette', 'russian'])
async def rr(ctx):
    await ctx.send(deal.rr(ctx.author.mention))


@rr.error
async def rr_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandError):
        await ctx.send(random.choice(deal.rr_fails))


# KILL
@bot.command(aliases=['murder', 'assassinate', 'attack'])
async def kill(ctx, user: discord.Member = None):
    if user and user != ctx.author:
        await ctx.send(deal.kill(ctx.author.mention, user.mention))
    else:
        await ctx.send("Are you... trying to kill yourself? Consider me impressed.")


@kill.error
async def kill_error(ctx, error):
    if isinstance(error, discord.ext.commands.BadArgument):
        await ctx.send(random.choice(deal.kill_fails))


# REVIVE
@bot.command(aliases=['save', 'rev'])
async def revive(ctx, user: discord.Member = None):
    if user:
        await ctx.send(deal.revive(ctx.author.mention, user.mention))


@revive.error
async def revive_error(ctx, error):
    if isinstance(error, discord.ext.commands.BadArgument):
        await ctx.send(random.choice(deal.revive_fails))

# ----------------------------------------------------------------------------------------------------------------------


# TOKEN / SIGNING IN
with open('config.json') as config_file:
    config_dict = json.load(config_file)

bot.run(config_dict["bot_token"])
