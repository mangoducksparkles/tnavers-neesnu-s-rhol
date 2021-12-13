import os
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='!', case_insensitive=True)
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def c(ctx, *, msg):
	await ctx.send(msg[::-1], tty=True)
	await ctx.message.delete()

if __name__ == "__main__":
	bot.run(TOKEN)
