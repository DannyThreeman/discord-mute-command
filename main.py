import discord   #Discord compositer
from discord.ext import commands

client = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Bot byl přihlášen jako {client.user}')
    
@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, user: discord.Member):
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted")   #Must create role "Muted" on your discord server
    await user.add_roles(mute_role)
    await ctx.send(f'Hráč jménem {user} byl zlumen!')
    await ctx.message.delete()
    
    
@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, user: discord.Member):
    mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
    await user.remove_roles(mute_role)
    await ctx.send(f'Hráč jménem {user} může opět psát do chatu!')
    await ctx.message.delete()
    
client.run('<Bot token here>')
