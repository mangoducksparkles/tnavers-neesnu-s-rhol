import os
from discord.ext import commands
import discord
from gtts import gTTS
from io import BytesIO

bot = commands.Bot(command_prefix='!', case_insensitive=True)
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def join(ctx):
	try:
		channel = ctx.message.author.voice.channel
		await channel.connect()
		return
	except Exception as e:
		print(e)
		await ctx.send("Cannot connect to voice channel")
		return

@bot.command()
async def leave(ctx):
	try:
		await ctx.voice_client.disconnect(force=True)
		return
	except Exception as e:
		print(e)
		await ctx.send("Cannot disconnect from voice channel")
		return

@bot.command()
async def c(ctx, *, msg):
	try:
		msg = msg[::-1]
		vc = ctx.voice_client
		if vc is None || !vc.is_connected():
			await ctx.send(msg, tts=True)
		else:
			tts = gTTS(msg)
			bio = BytesIO()
			tts.write_to_fp(bio)
			vc.play(discord.FFmpegPCMAudio(bio, pipe=True))
		await ctx.message.delete()
		return
	except Exception as e:
		print(e)
		await ctx.send("Could not speak")
		return

if __name__ == "__main__":
	bot.run(TOKEN)
