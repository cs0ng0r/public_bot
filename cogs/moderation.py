import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderáció sikeresen betöltve!')

    @app_commands.command(name='ban', description='Felhasználó kitiltása.')
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        await member.ban(reason=reason)
        await interaction.response.send_message(f'{member.mention} sikeresen kitiltva.', ephemeral=True)

    @app_commands.command(name='kick', description='Felhasználó kirúgása.')
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        await member.kick(reason=reason)
        await interaction.response.send_message(f'{member.mention} sikeresen kirúgva.', ephemeral=True)

    @app_commands.command(name='mute', description='Felhasználó némítása.')
    @app_commands.checks.has_permissions(moderate_members=True)
    async def mute(self, interaction: discord.Interaction, member: discord.Member, duration: int, reason: str = None):
        await member.timeout(discord.utils.utcnow() + discord.timedelta(minutes=duration), reason=reason)
        await interaction.response.send_message(f'{member.mention} némítása {duration} percre sikeres.', ephemeral=True)

    @app_commands.command(name='unmute', description='Felhasználó némításának feloldása.')
    @app_commands.checks.has_permissions(moderate_members=True)
    async def unmute(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        await member.timeout(None, reason=reason)
        await interaction.response.send_message(f'{member.mention} némítása feloldva.', ephemeral=True)

    @app_commands.command(name='clear', description='Üzenetek törlése egy csatornából.')
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clear(self, interaction: discord.Interaction, amount: int):
        deleted = await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f'{len(deleted)} üzenet sikeresen törölve.', ephemeral=True)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
