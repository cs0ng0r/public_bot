import discord
from discord.ext import commands
from config import IDEA_CHANNEL_ID

class AutoReact(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('AutoReaction sikeresen betöltve!')

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return

        if message.channel.id == IDEA_CHANNEL_ID and not isinstance(message.channel, discord.Thread):
            # Beágyazott üzenet létrehozása
            embed_message = discord.Embed(
                title='Ötlet',
                description=message.content,
                color=discord.Color.orange()
            )
            embed_message.set_author(
                name=message.author.display_name,
                icon_url=message.author.avatar.url
            )

            # Eredeti üzenet törlése
            await message.delete()

            # Elküldeni az új üzenetet
            new_message = await message.channel.send(embed=embed_message)

            # Reackciók hozzáadása
            await new_message.add_reaction('✅')
            await new_message.add_reaction('❌')

async def setup(bot):
    await bot.add_cog(AutoReact(bot))
