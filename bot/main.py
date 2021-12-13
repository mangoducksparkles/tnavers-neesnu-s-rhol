import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!", case_insensitive=true)
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def c(ctx, *, msg):
    await ctx.send(msg.reverse(), tty=true)
	await ctx.message.delete()

if __name__ == "__main__":
    bot.run(TOKEN)
