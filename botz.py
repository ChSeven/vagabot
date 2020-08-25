import discord
import os
from discord.ext import commands

client =commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready")
    
@client.command()
async def hello(ctx):
    await ctx.send("Hi there!")
@client.command()
async def F(ctx):
    await ctx.send("You have paid your respects")

@client.command()
async def Modi(ctx):
    await ctx.send("Mitron..!!")    
     
client.run("vNzQzMTAzOTA1NTc0OTQ0ODM4.XzPzcQ.Uo6vuR0tH6J37QoBmx1EtbG5J8Y)
