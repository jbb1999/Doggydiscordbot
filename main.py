import discord
import config
from discord.ext import commands



bot = commands.Bot(config.command_prefix)




@bot.event
async def on_ready():
    if str(config.playing_true) == 'true':
            await bot.change_presence(activity=discord.Game(name=config.playing_name))


#user pinged
@bot.event
async def on_message(message):
    mention = f'<@!{c}>'
    if mention in message.content:
        await message.channel.send("You are now allowed to mention this user")
        await channel.send(f'{str(ctx.author)} has just pinged person.')


#invites
async def on_message(message):
    if message.author != c.user:
        if message.contains("discord.gg")
            await message.delete()
            await message.channel.send('Invites are not allowed')
    await bot.process_commands(message)

bot.run(config.token)