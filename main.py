#----------imports & froms----------#
import discord
import discord_components
import asyncio
import string
import datetime
import random
from discord.ext import commands
from discord_components import Button, Select, SelectOption, ComponentsBot, interaction
from discord_components.component import ButtonStyle
from discord.utils import get
#----------imports & froms----------#


#---------Complete this-------#
TOKEN =""
PREFIX ="-"
#---------Complete this-------#


#----------clients----------#
client = ComponentsBot(PREFIX, help_command=None)
#----------clients----------#

#----------on ready----------#
@client.event
async def on_ready():
    print("Bot Is Ready")
#----------on ready----------#


#---------code---------#
@client.command()
@commands.has_permissions(administrator=True)
async def gen(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Welcome to password generator menu.", description="Please select your choice from buttons below/", color=discord.Color.dark_gray())
    await ctx.send(embed=embed,

            components = [[
                Button(custom_id = '1',label = "Strong",style = ButtonStyle.green,emoji ='💪'),
                Button(custom_id = '2', label = "Normal", style = ButtonStyle.blue,emoji='🧰'),
                Button(custom_id = '3', label="Weak", style = ButtonStyle.gray,emoji='📌')]])

@client.event
async def on_button_click(interaction):
    if interaction.component.custom_id == "1":
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""   
        for index in range(12):
            password = password + random.choice(characters)

        embedr = discord.Embed(title="Password generated.")
        embedr.add_field(name="Type:",value="Strong")
        embedr.add_field(name="Characters:",value="12")
        embedr.add_field(name="Password:",value=password, inline=False)
        await interaction.send(embed=embedr, delete_after= 3)
    if interaction.component.custom_id == "2":
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""   
        for index in range(8):
            password = password + random.choice(characters)

        embedr = discord.Embed(title="Password generated.")
        embedr.add_field(name="Type:",value="Normal")
        embedr.add_field(name="Characters:",value="8")
        embedr.add_field(name="Password:",value=password, inline=False)
        await interaction.send(embed=embedr, delete_after= 3)
    if interaction.component.custom_id == "3":
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""   
        for index in range(4):
            password = password + random.choice(characters)

        embedr = discord.Embed(title="Password generated.")
        embedr.add_field(name="Type:",value="Weak")
        embedr.add_field(name="Characters:",value="4")
        embedr.add_field(name="Password:",value=password, inline=False)
        await interaction.send(embed=embedr, delete_after= 3)
#---------code---------#

#----------run----------#
client.run(TOKEN)