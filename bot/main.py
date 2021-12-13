import os
from discord.ext import commands
import discord
from gtts import gTTS
from io import BytesIO

bot = commands.Bot(command_prefix='!', case_insensitive=True)
TOKEN = os.getenv('DISCORD_TOKEN')
vc = None

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def join(ctx):
	try:
        channel = ctx.message.author.voice.channel
        await channel.connect()
		vc = channel
        return
    except Exception as e:
		print(e)
        await ctx.send("Cannot connect to voice channel")
        return

@bot.command()
async def leave(ctx):
	try:
        await ctx.voice_client.disconnect(force=True)
		vc = None
        return
    except Exception as e:
		print(e)
        await ctx.send("Cannot disconnect from voice channel")
        return

@bot.command()
async def c(ctx, *, msg):
	try:
		msg = msg[::-1]
		if vc is None:
			await ctx.send(msg, tts=True)
			await ctx.message.delete()
		else:
			tts = gTTS(msg)
			bio = BytesIO()
			tts.write_to_fp(bio)
			vc.play(discord.FFmpegPCMAudio(bio, pipe=True))
	except Exception as e:
		print(e)
		await ctx.send("Could not speak")

if __name__ == "__main__":
	bot.run(TOKEN)
