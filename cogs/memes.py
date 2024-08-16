import discord
from discord.ext import commands
from random import choice
import asyncpraw as praw
from config import MEME_CHANNEL_ID


class Reddit(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        # https://www.reddit.com/prefs/apps oldalon tudjátok létrehozni a saját alkalmazásotokat
        self.reddit = praw.Reddit(
            client_id='',
            client_secret='',
            user_agent='')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Memek sikeresen betöltve!')

    @commands.command()
    async def meme(self, ctx: commands.Context, subreddit_name: str = 'memes'):
        # Megfelelő csatorna ellenőrzése
        if ctx.channel.id != MEME_CHANNEL_ID:
            return await ctx.send(
                'Ezt a parancsot csak a megfelelő csatornában használhatod!')

        print(f'Subreddit fetchelése: {subreddit_name}')
        subreddit = await self.reddit.subreddit(subreddit_name)
        posts_list = []

        print('Posztok gyűjtése...')
        async for post in subreddit.top(limit=25):
            if not post.over_18 and post.author is not None and any(
                    post.url.endswith(ext)
                    for ext in ['.jpg', '.png', '.jpeg', '.gif']):
                author = post.author.name
                posts_list.append((post.url, author))
            elif post.author is None:
                posts_list.append((post.url, 'Nincs szerző'))

        print(f'Talált posztok szama: {len(posts_list)}')

        if posts_list:
            if post.over_18:
                print(f'NSFW tartalmat kért le {ctx.author.name}')
                return
            meme_url, author = choice(posts_list)
            meme_embed = discord.Embed(color=discord.Color.green())
            meme_embed.set_author(name=f'Meme lekérve {ctx.author.name} által',
                                  icon_url=ctx.author.avatar.url)
            meme_embed.set_image(url=meme_url)
            meme_embed.set_footer(text=f'Eredeti szerző: {author}')
            await ctx.send(embed=meme_embed)
            print('Elküldve')
        else:
            await ctx.send('Nem találtam memét!')
            print('Nem találtam mémet')

    def cog_unload(self):
        self.bot.loop.create_task(self.reddit.close())


async def setup(bot):
    await bot.add_cog(Reddit(bot))
