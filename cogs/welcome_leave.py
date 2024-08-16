import discord
from discord.ext import commands
from config import WELCOME_CHANNEL_ID, LEAVE_CHANNEL_ID


class WelcomeLeave(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Join-Leave sikeresen betöltve!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(WELCOME_CHANNEL_ID)
        join_embed = discord.Embed(
            title=f'{member.mention} csatlakozott a szerverhez!',
            description='Kérlek olvassad el a szabályzatot!',
            color=discord.Color.green())
        join_embed.set_thumbnail(url=member.avatar_url)
        join_embed.set_footer(text=f'{member.guild.name}',
                              icon_url=member.guild.icon_url)
        await channel.send(embed=join_embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(LEAVE_CHANNEL_ID)
        leave_embed = discord.Embed(
            title=f'{member.mention} elhagyta a szervert!',
            description='Várunk vissza!',
            color=discord.Color.red())
        leave_embed.set_thumbnail(url=member.avatar_url)
        leave_embed.set_footer(text=f'{member.guild.name}',
                               icon_url=member.guild.icon_url)
        await channel.send(embed=leave_embed)


async def setup(bot):
    await bot.add_cog(WelcomeLeave(bot))
