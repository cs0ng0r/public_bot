import discord
from discord.ext import commands


class Parancsok(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Parancsok sikeresen betöltve!')

    @commands.command(aliases=['botping'])
    async def ping(self, ctx):
        ping_embed = discord.Embed(title='Bot Ping',
                                   color=discord.Color.green())
        ping_embed.add_field(name='Késleltetés:',
                             value=f'{round(self.bot.latency * 1000)}ms')
        ping_embed.set_footer(text=f'Lefuttatva: {ctx.author} által',
                              icon_url=ctx.author.avatar)
        await ctx.send(embed=ping_embed)


async def setup(bot):
    await bot.add_cog(Parancsok(bot))
